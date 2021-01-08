@def title = "Vectorization"
@def hascode = true
@def rss = "Specifically, why you should vectorize your code, when you should vectorize your code, and how you should vectorize your code."
@def rss_title = "Vectorization"
@def rss_pubdate = Date(2021, 1, 7)


Specifically, why you should vectorize your code, when you should vectorize your code, and how you should vectorize your code.  

\tableofcontents

## SIMD

@@row
@@container
@@ ![SIMD processable vs. unprocessable](/assets/SIMD_processable_vs_unprocessable.png) @@
@@
This is a photo
~~~
<div style="clear: both"></div>
~~~
@@

@@row
@@container
@@ ![](/assets/SIMD_vs_scalar.png) @@
@@
SIMD processable vs. unprocessable
~~~
<div style="clear: both"></div>
~~~
@@

@@row
@@container
@@left ![](/assets/rndimg.jpg) @@
@@
Marine iguanas are **truly splendid** creatures. They're not found in equations like $\exp(-i\pi)+1$. But they're still quite cool.
~~~
<div style="clear: both"></div>
~~~
@@

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

@def hasplotly = true
```julia:ex1
using PlotlyJS
z =  [10     10.625  12.5  15.625  20
     5.625  6.25    8.125 11.25   15.625
     2.5    3.125   5.    8.125   12.5
     0.625  1.25    3.125 6.25    10.625
     0      0.625   2.5   5.625   10]

data   = contour(; z=z)
layout = Layout(; title="Basic Contour Plot")
plt    = plot(data, layout)

fdplotly(json(plt)) # hide
```
\textoutput{ex1}

@@info
    Use blue boxes (alert-info) for tips and notes.
@@

@@warning
    Use yellow boxes for examples that are not inside code cells, or use for mathematical formulas if needed. Typically also used to display warning messages.
@@

@@success
    This alert box indicates a successful or positive action.
@@

@@error
    This alert box indicates a dangerous or potentially negative action.
@@

@@note
    this is a note
@@