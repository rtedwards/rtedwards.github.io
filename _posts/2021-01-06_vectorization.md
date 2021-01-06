# Vectorization

Specifically, why you should vectorize your code, when you should vectorize your code, and how you should vectorize your code.  

1. TOC
{:toc}

## SIMD

![SIMD processable vs. unprocessable](images/SIMD_processable_vs_unprocessable.png)

![SIMD processable vs. unprocessable](images/SIMD_vs_scalar.png)

```python
a = [1, 2, 3, 4]
b = [1, 1, 2, 2]

c = [a[i] * b[i] for i, _ in enumerate(a)]

# c = [1, 2, 6, 8]
```

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 1, 2, 2])

c = a * b

# c = array([1, 2, 6, 8])
```