+++
title = "When Eye-Balling It Is Good Enough"
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

**TODO:** (Add altair plot of linear regression and residuals on [formaldehyde dataset](https://rowannicholls.github.io/R/data/datasets/Formaldehyde.html))
- [Altair scatterplot regression](https://altair-viz.github.io/gallery/poly_fit_regression.html)
- [Altair scatterplot with error bars](https://altair-viz.github.io/gallery/simple_scatter_with_errorbars.html)

In my statistics degree, we were told that a visual inspect of the Q-Q plot (residual plot) was enough
to determine if the residuals were Normally distributed.  However, there are tests for determining if
a data sample is Normally distributed, or from a chosen distribution. **Talk about tests a bit**.
I'm not sure if we were told that _eye-balling it_ was an appropriate method about as good as statistical
tests or if more rigorous checks just weren't practical to ask during an exam.

## Visual Inspection
So let's try _eye-balling it_.  Below are 1,000 samples from 6 different distributions.  Can you tell
which distributions were sampled from?  Which look Normally distributed?

<p style="text-align:center;">
    <img
        src="/assets/eye_balling_it/eye-balling-distributions-1000.svg"
        style="border:0px #ffffff none; border-radius: 10px;"
        alt="eye-balling some distributions"
    >
</p>

Just so it wasn't obvious due in some cases due to bounds, the means of each sample have been centered on zero.



Now which are which

<p style="text-align:center;">
    <img
        src="/assets/eye_balling_it/distributions-revealed-1000.svg"
        style="border:0px #ffffff none; border-radius: 10px;"
        alt="eye-balling some distributions"
    >
</p>

By taking the [z-score normalization](https://en.wikipedia.org/wiki/Standard_score) of each we can visually
compare within the same plot.  We already set the means to zero so the only difference here is transforming
each to have a standard deviation of 1.

<center>
<iframe
    src="/assets/eye_balling_it/normalized-combined-1000.html"
    style="border:0px #ffffff none; border-radius: 10px;"
    name="myiFrame"
    scrolling="no"
    frameborder="1"
    marginheight="0px"
    marginwidth="0px"
    height="385px"
    width="675px"
    allowfullscreen>
</iframe>
</center>

## Statistical Tests
Beyond visual inspection what can we do to check if a sample is from a distribution?  Fortunately for us,
there's a statistical test for just about everything.  The [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)
(KS-test) is a nonparametric test that can be used to compare a sample to a distribution by answering the
question "how likely is a sample to have been drawn from a given probability distribution?"

$$KS = ???$$

_Why don't we use a t-test and call it a day?_  A one-sided [t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)
only compare the mean of a sample to the null hypothesis.  The KS-test is sensitive to differences in
both location (mean) and shape of the empirical CDF of the sample.  If you've ever seen (this plot)
**TODO: find plot** it's simple to recognize that comparing means is not enough.

- KSTests
- code
- confidence intervals?
- credible intervals?

## Regression to Fit Parameters
- KS test for goodness of fit

### Check Errors Are Normally Distributed
- a relevant example for this blog!
- need to check errors are Normally distributed because if not then parameters may be unstable
-

## Is Eye-Balling It Good Enough?
- For Normal distribution, yes.  It's used all the time in Q-Q plots for regressions.
- For other distributions, probably not.  The Normal distribution is symmetric and very recognizable,
    other distributions can change drammatically with different parameters
    - examples of different parameters for distributions 2x6 plot
    - worth testing
- Sample size (n>?)

Resources:
- [Testing Distributions](https://datascienceinpractice.github.io/tutorials/11-TestingDistributions.html)
- [Scipy normaltest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html#scipy.stats.normaltest)
- [Scipy kstest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html#scipy.stats.kstest)
- [Scipy shapiro-wilk test](www.google.com)
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3693611/

Footnotes:
- [0] When doing multiple statistical tests, a multiple comparisons correction should be added.
    A 95% confidence level, $\alpha=0.05$, means that 1 in 20 statistical tests are incorrect, on average.
- [1]
- [2] [Introduction to Statistical Learning](https://www.statlearning.com/)
- [3] [Elements of Statistical Learning](https://hastie.su.domains/Papers/ESLII.pdf)
