+++
title = "Why Vega Is Mega"
date = 2023-03-25
description = "The case for VegaLite as your default plotting engine."
summary = "The case for VegaLite as your default plotting engine."
draft = true

[taxonomies]
tags = ["python"]

[extra]
katex = true
+++

> “The greatest value of a picture is when it forces us to notice what we never expected to see.” \
> \
>  ― John Tukey, 1977

> “Comparisons must be enforced within the scope of the eyespan, a fundamental point occasionally forgotten in practice.”
> \
> ― Edward Tufte


\
\

In statistics (and by the transitive property data science) it's important to visualize the data.  When
data is visualized, unknown and unseen trends may appear and previously held assumptions may be invalidated.

- **Sensor analogy**
- **anecdote**

[VegaLite](https://vega.github.io/vega-lite/) is a light-weight visualization specification from the
University of Washington [Interactive Data Lab](https://idl.cs.washington.edu/).  It is based on the
[Vega](https://vega.github.io/vega/) specification.

<p style="text-align:center;">
    <img
        src="/assets/why_vega_is_mega/gglayers.png"
        style="border:0px #ffffff none; border-radius: 10px;"
        alt="animated vega-lite"
    >
</p>
<center>
    <font size="1">
        Pilfered from
        <a href="https://r.qcbs.ca/workshop03/book-en/grammar-of-graphics-gg-basics.html">Quebec Center for Biodiversity Science</a>
        which is itself adapted from
        <a href="https://link.springer.com/book/10.1007/0-387-28695-0">Grammar of Graphics</a>.
    </font>
</center>

- [Vega is deployed on Wikipedia](https://www.mediawiki.org/wiki/Extension:Graph) to define
visualizations directly within wiki pages.

## Why I use Vega Lite
- **Intuitive and consise** - Being based on Grammar of Graphics, the API feels like set of buildings blocks.
- **Visual design grounded in research** - Default colorschemes are selected via
    [academic research](https://idl.cs.washington.edu/files/2018-QuantitativeColor-CHI.pdf).  (The charts throughout
    this blog may have a slightly modified colorscheme, but not in this post).
- **Interactive** -
- **Performant** - Has [reactive dataflows](https://observablehq.com/@vega/how-vega-works) allowing for
    efficient reactive updates. When parameters change or the input data is modified, only nodes affected
    by the update are re-evaluated.
- **Portable** - Has bindings for every major language, can be fully described in JSON, and is familiar to
    use in any language.
- **Looks great out of the box** - Can create professional-looking graphs in a few lines.
    Offers deep customization for statistical graphs.  Has escape hatches for more fine-grained control
    through Vega.
- **Free and open-source** - [Github](https://github.com/vega/vega-lite)
- **Ubiquitous.**  Vega Lite is in [Wikipedia](https://www.mediawiki.org/wiki/Extension:Graph),
    [Pandas](https://pandas.pydata.org/docs/ecosystem.html?highlight=vega#altair),
    [JupyterLab](https://github.com/jupyterlab/jupyterlab/tree/bddc378b72e8ee78be8b6e2ffb2b527a75f0471a/packages/vega5-extension),
    and [so so many more](https://vega.github.io/vega-lite/ecosystem.html).

## An Example
I'm using Altair and Python here but the code looks almost identical in other languages.

```python
import altair as alt
from vega_datasets import data

source = data.cars()

graph = (
    alt.Chart(source) # the data
    .mark_circle() # plot points
    .interactive() # make it zoomable / scrollable
    .encode( # set the data fields
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color='Origin:N'
    ).properties( # properties for each sub-chart
        width=150,
        height=150
    ).repeat( # describes categories to permutate across rows / cols
        row=['Horsepower', 'Acceleration', 'Miles_per_Gallon'],
        column=['Miles_per_Gallon', 'Acceleration', 'Horsepower']
    ).configure( # everything in configure is styling
        background="#202124",
        view=alt.ViewConfig(stroke="transparent"),
        axis=alt.AxisConfig(
            labelFont="monospace",
            titleFont="monospace",
            titleColor="white",
            labelColor="white",
            tickColor="white",
            gridColor="grey",
            domainColor="white",
        ),
        legend=alt.LegendConfig(
            labelFont="monospace",
            titleFont="monospace",
            labelColor="white",
            titleColor="white",
        ),
        title=alt.TitleConfig(
            font="monospace",
            color="white",
        )
    )
    .properties(padding=20) # extra padding for blog
)

graph
```
<center>
    <iframe
        src="/assets/why_vega_is_mega/interactive-scatter-matrix.html"
        style="border:0px #ffffff none; border-radius: 10px;"
        name="myiFrame"
        scrolling="no"
        frameborder="1"
        marginheight="0px"
        marginwidth="0px"
        height="635px"
        width="725px"
        allowfullscreen>
    </iframe>
</center>
<center>
    <font size="1">It's interactive!  Go ahead and zoom / scroll.  Double click to reset.</font>
</center>

## Grammar of Graphics projects
- [Grammar of Graphics](https://link.springer.com/book/10.1007/0-387-28695-0)
- Hadley Wickham's [A Layered Grammar of Graphics](https://vita.had.co.nz/papers/layered-grammar.html)
- [VegaLite: A Grammar of Interactive Graphics](https://idl.cs.washington.edu/papers/vega-lite)
- [Altair](https://altair-viz.github.io/) - Python implementation of VegaLite

## Interesting projects that build on Vega and GoG
**[Gemini: A Grammar and Recommender System for Animated Transitions in Statistical Graphics](https://idl.cs.washington.edu/papers/gemini)**
- UW IDL
- Animated VegaLite

<p style="text-align:center;">
    <img
        src="/assets/why_vega_is_mega/gemini-example.gif"
        style="border:0px #ffffff none; border-radius: 10px;"
        alt="animated vega-lite"
    >
    <img
        src="/assets/why_vega_is_mega/gemini-example-2.gif"
        style="border:0px #ffffff none; border-radius: 10px;"
        alt="animated vega-lite"
    >
</p>


**[Animated Vega-Lite: Unifying Animation with a Grammar of Interactive Graphics](https://vis.csail.mit.edu/pubs/animated-vega-lite/)**
- MIT CSAIL
- Animated & interactive VegaLite

<p style="text-align:center;">
    <img
        src="/assets/why_vega_is_mega/animated-vegalite.gif"
        style="border:0px #ffffff none; border-radius: 10px;"
        alt="animated vega-lite"
    >
</p>

**[Probabilistic Grammar of Graphics](https://www.mjskay.com/papers/chi2020-pgog.pdf)**
- University of Michigan
- VegaLite for probabilistic data representations
