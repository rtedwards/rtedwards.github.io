+++
title = "Idiomatic Pandas"
date = 2023-07-23
description = "How to write idiomatic pandas and how it avoids footguns"
draft = true

[taxonomies]
tags = ["python", "performance", "pandas", "data science"]

[extra]
katex = true
+++

- [Enhancing Performance](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)
- [Copy On Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)

[Pandas](https://pandas.pydata.org/) is great!  It's helped make Python the de facto language for data science and
machine learning by enabling data scientists and analysts a _relatively_ intuitive
and simple way to munge, clean, and transform datasets.

But it's not perfect.  There's more than one way to skin a cat with Pandas and it's not
always obvious which way to use and when.  I'm going to lay out a subjective view how Pandas
should be written and try to back up my opionions with objective reasoning, science,
and experiences so you can learn how to write better Pandas.

```python
df = pd.DataFrame({
    "name": ["robert", "john", "david"],
    "age":  [32, 32, 32]
})
```
