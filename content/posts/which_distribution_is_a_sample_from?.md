+++
title = "Which distribution is a sample from?"
date = 2023-07-29
description = "Which distribution is a sample from?"

[taxonomies]
tags = ["data science", "pandas", "python", "statistics"]

[extra]
katex = true
+++

I recently came across an interesting problem at work.  While synthesizing a dataset akin to
one of our real datasets we modelled the noise as Normal.   Seems like a fair assumption without
prior knowledge about the noise.  But _was our assumption valid_?  How do we check if it's Normal
and if not how can we determine another distribution that better models the noise?

In statistics, linear (and non-linear) regression models are based on the assumption that the
residuals (or errors in machine learning circles), the difference between model predictions and
observed data, are Normally distributed.  This is because $\beta$ **rest of the owl explaination**.  For a an actually rigorous
explaination, I'll point you to any intro to stats book [1][2][3].

(Add altair plot of linear regression and residuals on [formaldehyde dataset](https://rowannicholls.github.io/R/data/datasets/Formaldehyde.html))
- [Altair scatterplot regression](https://altair-viz.github.io/gallery/poly_fit_regression.html)
- [Altair scatterplot with error bars](https://altair-viz.github.io/gallery/simple_scatter_with_errorbars.html)

In my statistics degree, we were told that a visual inspect of the Q-Q plot (residual plot) was enough
to determine if the residuals were Normally distributed.  However, there are tests for determining if
a data sample is Normally distributed, or from a chosen distribution. **Talk about tests a bit**.
I'm not sure if we were told that _eye-balling it_ was an appropriate method about as good as statistical
tests or if more rigorous checks just weren't practical to ask during an exam.

- [1]
- [2] [Introduction to Statistical Learning](https://www.statlearning.com/)
- [3] [Elements of Statistical Learning](https://hastie.su.domains/Papers/ESLII.pdf)

-----
