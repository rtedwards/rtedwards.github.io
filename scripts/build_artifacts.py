"""Run the Python behind the posts and write the results the Astro site imports.

Outputs go to site/src/generated/<post-slug>/ and are committed: Cloudflare
Pages cannot run this environment, so the site build only reads these files.
Run through `just site-artifacts`.
"""

import json
from pathlib import Path

import altair as alt
import numpy as np
import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "site" / "src" / "generated"


def metadata_size_chart(df: pl.DataFrame, subtitle: str) -> alt.Chart:
    """Metadata size against column count, one line per row group size and name length."""
    colors = ["#368BC1", "#F2BB18", "#BB4430", "#8A9A67", "#CC771F", "#8B5260"]
    return (
        alt.Chart(df)
        .mark_line(size=2, point=True)
        .encode(
            x=alt.X("num_cols", title="Number of Columns"),
            y=alt.Y("metadata_size_mb", title="Metadata Size (MB)").scale(type="log"),
            color=alt.Color(
                "row_group_size:N",
                title="Row Group Size",
                scale=alt.Scale(range=colors),
            ),
            strokeDash=alt.Shape("col_name_lengths:N", title="Column Name Length (chars)"),
            opacity=alt.value(1.0),
        )
        .properties(
            title={
                "text": ["Parquet metadata sizes for a single file of float columns"],
                "subtitle": [subtitle],
            },
            width=650,
            padding=10,
        )
    )


FULL_WRITE = {}
REDUCED_WRITE = {"write_statistics": False, "store_schema": False, "use_dictionary": False}


def metadata_bytes(table: pa.Table, row_group_size: int, write_options: dict) -> int:
    """Write a table to memory and return the size of its Parquet footer metadata."""
    sink = pa.BufferOutputStream()
    pq.write_table(
        table,
        sink,
        compression="zstd",
        compression_level=9,
        row_group_size=row_group_size,
        **write_options,
    )
    return pq.ParquetFile(pa.BufferReader(sink.getvalue())).metadata.serialized_size


def metadata_sweep(write_options: dict) -> pl.DataFrame:
    """The sweep from the post: columns, name length and row group size against metadata size."""
    rng = np.random.default_rng(0)
    rows = []
    for num_cols in [1, 10, 50, 100, 150]:
        for name_length in [1, 10, 50, 100]:
            col_name = "x" * name_length
            data = {f"{x}{col_name}": rng.random(1_000) for x in range(num_cols)}
            table = pl.DataFrame(data).to_arrow()
            for row_group_size in [1_000, 100, 10, 1]:
                rows.append({
                    "num_cols": num_cols,
                    "row_group_size": row_group_size,
                    "col_name_lengths": name_length,
                    "metadata_size_b": metadata_bytes(table, row_group_size, write_options),
                })
    return pl.DataFrame(rows).with_columns(
        (pl.col("metadata_size_b") / 1024**2).alias("metadata_size_mb"),
    )


def parquet_metadata(out_dir: Path) -> None:
    rng = np.random.default_rng(0)

    # The single-file numbers quoted in the post: 15 columns with row group size 10,
    # and 150 columns with row group size 1, then the same 150 columns with reduced metadata.
    table_15 = pl.DataFrame({f"{x}": rng.random(1_000) for x in range(15)}).to_arrow()
    table_150 = pl.DataFrame({f"{x}": rng.random(1_000) for x in range(150)}).to_arrow()
    small = metadata_bytes(table_15, 10, FULL_WRITE)
    large = metadata_bytes(table_150, 1, FULL_WRITE)
    reduced = metadata_bytes(table_150, 1, REDUCED_WRITE)

    stats = {
        "small_bytes": small,
        "small_mb": round(small / 1024**2, 2),
        "large_bytes": large,
        "large_mb": round(large / 1024**2, 1),
        "reduced_bytes": reduced,
        "reduced_mb": round(reduced / 1024**2, 1),
        "reduced_pct_of_large": round(100 * reduced / large),
        "reduction_pct": round(100 * (1 - reduced / large)),
        # 2,000 files at the single-file size, for 4 GPUs with 2 workers each, in GiB.
        "files": 2_000,
        "processes": 8,
        "per_process_gb": round(2_000 * large / 1024**3),
        "total_gb": round(8 * 2_000 * large / 1024**3),
    }
    (out_dir / "stats.json").write_text(json.dumps(stats, indent=2))

    default = metadata_sweep(FULL_WRITE)
    chart = metadata_size_chart(default, subtitle="")
    (out_dir / "metadata_by_columns.json").write_text(json.dumps(chart.to_dict(), indent=2))

    reduced_sweep = metadata_sweep(REDUCED_WRITE)
    chart = metadata_size_chart(
        reduced_sweep,
        subtitle="No statistics, no dictionary encoding, no arrow schema",
    )
    (out_dir / "metadata_reduced.json").write_text(json.dumps(chart.to_dict(), indent=2))
    print(json.dumps(stats, indent=2))

def summing_random_variables(out_dir: Path) -> None:
    """Simulate the pub quiz problem: sum of independent normals, and the full y* model."""
    rng = np.random.default_rng(0)
    n = 100_000
    colors = ["#368BC1", "#F2BB18", "#BB4430", "#8A9A67", "#CC771F", "#8B5260"]

    err = rng.normal(0, 1, n)
    u = rng.normal(2, 2, n)  # u ~ N(2, 2): the second value is the standard deviation
    err_computational = err + u
    err_analytical = rng.normal(2, np.sqrt(5), n)

    def density(values: np.ndarray, label: str) -> pl.DataFrame:
        counts, edges = np.histogram(values, bins=120, range=(-6, 10), density=True)
        mids = (edges[:-1] + edges[1:]) / 2
        return pl.DataFrame({"x": mids, "density": counts, "series": [label] * len(mids)})

    densities = pl.concat([
        density(err, "err"),
        density(u, "u"),
        density(err_computational, "err* (computational)"),
        density(err_analytical, "err* (analytical)"),
    ])
    chart = (
        alt.Chart(densities)
        .mark_line()
        .encode(
            x=alt.X("x:Q", title=None),
            y=alt.Y("density:Q", title=None),
            color=alt.Color(
                "series:N",
                title="Random Variable",
                scale=alt.Scale(range=colors),
            ).legend(orient="top-right"),
        )
        .properties(
            width=650,
            padding=10,
            title={
                "text": f"Summing Two Independent Random Variables (n={n} samples)",
                "subtitle": "err + u = err*",
            },
        )
    )
    (out_dir / "density_chart.json").write_text(json.dumps(chart.to_dict(), indent=2))

    x = np.arange(0, 10, 0.01)
    err_measured = rng.normal(0, 1, len(x))
    y_measured = 3 + 2 * x + err_measured
    y_analytical = 5 + 2 * x + rng.normal(0, np.sqrt(5), len(x))
    y_computational = 3 + 2 * x + (err_measured + rng.normal(2, 2, len(x)))
    signal = 3 + 2 * x
    scatter = pl.concat([
        pl.DataFrame({"x": x, "y": signal, "dataset": ["signal (original)"] * len(x)}),
        pl.DataFrame({"x": x, "y": y_measured, "dataset": ["y"] * len(x)}),
        pl.DataFrame({"x": x, "y": y_computational, "dataset": ["y* (computational)"] * len(x)}),
        pl.DataFrame({"x": x, "y": y_analytical, "dataset": ["y* (analytical)"] * len(x)}),
    ])
    chart = (
        alt.Chart(scatter, title="Computational simulation of the problem matches the analytical solution")
        .mark_circle(size=10)
        .encode(
            x="x:Q",
            y="y:Q",
            color=alt.Color("dataset:N", title=None, scale=alt.Scale(range=colors)).legend(orient="top-left"),
        )
        .properties(width=650, padding=10)
    )
    (out_dir / "scatter_chart.json").write_text(json.dumps(chart.to_dict(), indent=2))

    rows = [
        ("ϵ", err),
        ("u", u),
        ("ϵ* (computational)", err_computational),
        ("ϵ* (analytical)", err_analytical),
    ]
    stats = [{"series": name, "mean": float(v.mean()), "var": float(v.var())} for name, v in rows]
    (out_dir / "stats.json").write_text(json.dumps({"n": n, "rows": stats}, indent=2))



def main() -> None:
    metadata = GENERATED / "parquet_metadata"
    metadata.mkdir(parents=True, exist_ok=True)
    parquet_metadata(metadata)

    summing = GENERATED / "summing_random_variables"
    summing.mkdir(parents=True, exist_ok=True)
    summing_random_variables(summing)

    print("wrote artifacts to site/src/generated/")


if __name__ == "__main__":
    main()
