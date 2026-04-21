import functools
import logging
import operator
import os
import time
from collections import Counter
from time import perf_counter as time

import torch
import torch.distributed as dist
import torch.multiprocessing as mp

from src.training.metrics import Metrics

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def reduce_tensor(rank: int, world_size: int) -> None:
    torch.distributed.init_process_group(
        backend="nccl"
        if torch.cuda.is_available()
        else "gloo",  # CPU only works on gloo backend
        rank=rank,
        world_size=world_size,
    )
    torch.cuda.set_device(rank)

    loss_tensor = torch.tensor([rank, rank]).cuda()
    print(loss_tensor)

    dist.reduce(loss_tensor, op=dist.ReduceOp.SUM, dst=0, async_op=True)
    print(loss_tensor)

    torch.distributed.destroy_process_group()


def all_reduce_tensor(rank: int, world_size: int) -> None:
    torch.distributed.init_process_group(
        backend="nccl"
        if torch.cuda.is_available()
        else "gloo",  # CPU only works on gloo backend
        rank=rank,
        world_size=world_size,
    )
    torch.cuda.set_device(rank)

    loss_tensor = torch.tensor([rank, rank]).cuda()
    print(loss_tensor)

    dist.all_reduce(loss_tensor, op=dist.ReduceOp.SUM, async_op=True)
    print(loss_tensor)

    torch.distributed.destroy_process_group()


def all_gather_object(rank: int, world_size: int) -> None:
    torch.distributed.init_process_group(
        backend="nccl"
        if torch.cuda.is_available()
        else "gloo",  # CPU only works on gloo backend
        rank=rank,
        world_size=world_size,
    )
    torch.cuda.set_device(rank)

    # pred = torch.tensor([[[[1.0, 0.0], [0.5, 0.0]]]])
    # target = torch.tensor([[[[1.0, 0.0], [0.0, 1.5]]]])
    # frac_threshold = 0.001
    # metrics = Metrics(frac_threshold).update(pred, target)

    losses = Counter(
        {
            "loss": 0.01,
            "binary_loss": 0.1,
            "conditional_loss": 0.001,
            "mse_loss": 0.5,
            "num_samples": rank + 1,
        }
    )
    print(losses)

    gather_list = [None for _ in range(world_size)]

    dist.all_gather_object(gather_list, losses)
    # sleep(2)
    losses = functools.reduce(operator.add, gather_list)

    print(losses)
    # print(metrics.as_dict())

    torch.distributed.destroy_process_group()


def gather_object(rank: int, world_size: int) -> None:
    torch.distributed.init_process_group(
        backend="nccl"
        if torch.cuda.is_available()
        else "gloo",  # CPU only works on gloo backend
        rank=rank,
        world_size=world_size,
    )
    torch.cuda.set_device(rank)

    pred = torch.tensor([[[[1.0, 0.0], [0.5, 0.0]]]])
    target = torch.tensor([[[[1.0, 0.0], [0.0, 1.5]]]])
    frac_threshold = 0.001
    metrics = Metrics(frac_threshold).update(pred, target)

    # losses = Counter(
    #     {"loss": 0.01, "binary_loss": 0.1, "conditional_loss": 0.001, "mse_loss": 0.5, "num_samples": rank + 1}
    # )
    print(metrics.as_dict())

    gather_list = [None for _ in range(world_size)]

    dist.gather_object(metrics, gather_list if rank == 0 else None, dst=0)

    if rank == 0:
        metrics = functools.reduce(operator.add, gather_list)

    print(metrics)

    torch.distributed.destroy_process_group()


def all_gather(rank: int, world_size: int) -> None:
    torch.distributed.init_process_group(
        backend="nccl"
        if torch.cuda.is_available()
        else "gloo",  # CPU only works on gloo backend
        rank=rank,
        world_size=world_size,
    )
    torch.cuda.set_device(rank)

    loss_tensor = torch.tensor([rank, rank]).cuda()

    logger.info(f"[GPU{rank}]: reducing")
    gather_list = [
        torch.zeros(2, dtype=torch.int64, device=torch.device(f"cuda:{rank}"))
        for _ in range(world_size)
    ]

    start = time()
    dist.all_gather(gather_list, loss_tensor)
    logger.warning(f"[GPU{rank}] all_gather: {time() - start} seconds")

    # if dist.get_rank() == 0:
    logger.info(gather_list)

    torch.distributed.destroy_process_group()


def gather(rank: int, world_size: int) -> None:
    torch.distributed.init_process_group(
        backend="nccl"
        if torch.cuda.is_available()
        else "gloo",  # CPU only works on gloo backend
        rank=rank,
        world_size=world_size,
    )
    torch.cuda.set_device(rank)

    loss_tensor = torch.tensor([rank, rank]).cuda()

    logger.info(f"[GPU{rank}]: gathering")

    gather_list = [
        torch.zeros(2, dtype=torch.int64, device=torch.device(f"cuda:{rank}"))
        for _ in range(world_size)
    ]

    dist.gather(loss_tensor, gather_list if rank == 0 else None, dst=0, async_op=False)
    if dist.get_rank() == 0:
        logger.info(gather_list)

    torch.distributed.destroy_process_group()


if __name__ == "__main__":
    os.environ["MASTER_ADDR"] = "localhost"
    os.environ["MASTER_PORT"] = "12345"
    # os.environ["TORCH_CPP_LOG_LEVEL"] = "INFO"
    # os.environ["TORCH_DISTRIBUTED_DEBUG"] = "DETAIL"

    num_gpu = torch.cuda.device_count()
    # mp.spawn(reduce_tensor, nprocs=num_gpu, args=(num_gpu,))
    # mp.spawn(all_reduce_tensor, nprocs=num_gpu, args=(num_gpu,))
    # mp.spawn(gather, nprocs=num_gpu, args=(num_gpu,))
    mp.spawn(gather_object, nprocs=num_gpu, args=(num_gpu,))
    # mp.spawn(all_gather, nprocs=num_gpu, args=(num_gpu,))
    # mp.spawn(all_gather_object, nprocs=num_gpu, args=(num_gpu,))
