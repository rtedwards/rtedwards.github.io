+++
title = "Why Vega Is Mega"
date = 2023-08-06
description = "The case for Vega-Lite as your default plotting engine."
summary = "The case for Vega-Lite as your default plotting engine."
draft = true

[taxonomies]
tags = ["python"]

[extra]
katex = true
+++

> “The greatest value of a picture is when it forces us to notice what we never expected to see.” \
> \
>  ― John Tukey, 1977

> “Comparisons must be enforced within the scope of the eyespan, a fundamental point occasionally forgotten in practice.” \
> \
> ― Edward Tufte


\
\

## Why the data needs to be visualized

In data science (and by transitive property ML) it's important to visualize the data so it can literally be
viewed in fresh perspectives.  When data is visualized, unknown and unseen trends may present themselves and previously
held assumptions about the data may be invalidated.

---: (Choose one or both and flesh out)
- **Sensor analogy**
- **anecdote**

[Anscombe's Quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) is a quartet of datasets that look identical
at first blush.  Each have the same mean, variance, correlation, and even the same regression statistics!  Based on
that statistics, one might reasonably assume that these datasets are all the same or have the same distirbution.
But they're completely different.  They don't even share the same distributions! [^1]

<p style="text-align:center;">
    <img
        src="/assets/why_vega_is_mega/anscombes-quartet.svg"
        style="border:0px #ffffff none; border-radius: 10px; float: right;"
        alt="animated vega-lite"
    >
</p>

| Property                      | Value               | Accuracy               |
|-------------------------------|---------------------|------------------------|
| x mean                        | 9.0                 | exact                  |
| x std dev                     | 11.0                | exact                  |
| y mean                        | 7.5                 | 2 decimal places       |
| x std dev                     | 4.125               | ±0.003                 |
| corr(x, y)                    | 0.816               | 3 decimal places       |
| Linear regression line        | y = 3.00 + 0.500x | 2 and 3 decimal places |
| Coeff of Determination: R^2   | 0.67                | 2 decimal places       |

\
\

How common is this phenomenon?  Is Anscombe's Quartet just a carefully crafted dataset?  Well the [Datasaurus Dozen](https://github.com/thomasp85/gganimate/wiki/The-Datasaurus-Dozen)
is another, even more extreme example.  These may be somewhat extreme examples, but any sufficiently complex dataset will
embody similar properties.

Anscombe's Quartet are small dataset with only two dimensions.  When datasets scale up it quickly becomes infeasible to create
charts for each view.  Big datasets become expensive to include all samples in a visualization, so instead a representative sample
is used.  Highly dimensional datasets explode in the number of interactions that must be viewed in 2D graphs.  High dimensionlity
is as much a problem for visualization as it is for modelling.  It's common to use dimensionality reduction techniques to reduce
complexity in these datasets.

---: (Blurb about need to visualize data and why to use a library that's fast, intuitive to use, and relatively easy to learn.
One that works with you not against you.  That feels like the correct tool for the job, not a hammer.)

## Grammar of Graphics
---: (Describe what Grammar of Graphics is and it's history)

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

## Why I use Vega-Lite
---: (Flesh out reasons more)

[Vega-Lite](https://vega.github.io/vega-lite/) is a light-weight visualization specification from the
University of Washington [Interactive Data Lab](https://idl.cs.washington.edu/).  It is based on the
[Vega](https://vega.github.io/vega/) specification.


[Why I'm Backing Vega-Lite](https://robinlinacre.medium.com/why-im-backing-vega-lite-as-our-default-tool-for-data-visualisation-51c20970df39)
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
- **Free and open-source** - It's right there on [Github](https://github.com/vega/vega-lite) along with
    [all the other language bindings](https://vega.github.io/vega-lite/ecosystem.html#bindings-for-programming-languages).
- **Ubiquitous.**  Vega-Lite is in [Wikipedia](https://www.mediawiki.org/wiki/Extension:Graph),
    [Pandas](https://pandas.pydata.org/docs/ecosystem.html?highlight=vega#altair),
    [JupyterLab](https://github.com/jupyterlab/jupyterlab/tree/bddc378b72e8ee78be8b6e2ffb2b527a75f0471a/packages/vega5-extension),
    and [so so many more](https://vega.github.io/vega-lite/ecosystem.html).

Vega-Lite is the first graphing tool I reach for with any statistical visualization, but it isn't the perfect tool for every job.
To create a wider array of visualization I might start reaching [Makie.jl](https://beautiful.makie.org/dev/)
or [D3.js](https://d3js.org/) for more bespoke ones[2].

## An appropriately complex example
The Vega-Lite [examples page](https://vega.github.io/vega-lite/examples/) has examples of just about any statistical graph you might want to make.

The following is an exploratory interactive graph of [Seattle weather](https://altair-viz.github.io/gallery/seattle_weather_interactive.html)
over the course of the year between 2012-2015.  It represents a sufficiently complex graph in terms of information density, data types, interactivity, and custom styling.

- Theme - custom colorscheme to reflect weather types
- Coordinates - x axis is a timeseries
- Statistics - bar chart of `weather` type
- Facets - not used here
- Geometries -  `precipication` dictates the size of the circles
- Aesthetics - `(x, y) -> (temp_max, date)`
- Data - the `source` dataframe

<center>
    <iframe
        src="/assets/why_vega_is_mega/seattle-weather.html"
        style="border:0px #ffffff none; border-radius: 10px;"
        name="myiFrame"
        scrolling="no"
        frameborder="1"
        marginheight="0px"
        marginwidth="0px"
        height="545px"
        width="750px"
        allowfullscreen>
    </iframe>
</center>
<center>
    <font size="1">
    It's interactive!  Go ahead and select a weather type in the bar chart or a brush selection on the date axis.
    Double click to reset.
    </font>
</center>

The code to produce is fairly arguably readable as a set of building blocks from the Grammar of Graphics.  Most data
visualizations tasks don't get much more complex than this.  I'm using Altair and Python here but the code looks almost
identical in other languages.

```python
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

# Custom colorscheme to reflect weather types
scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"]
)
color = alt.Color("weather:N", title="Weather", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_point(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_point().encode(
    alt.X("monthdate(date):T").title("Date"),
    alt.Y("temp_max:Q")
        .title("Maximum Daily Temperature (C)")
        .scale(domain=[-5, 40]),
    alt.Size("precipitation:Q", title="Precipitation (mm)").scale(range=[5, 200]),
    color=alt.condition(brush, color, alt.value("lightgray")),
).properties(
    width=550,
    height=300
).add_params(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of weather type
bars = alt.Chart().mark_bar().encode(
    x="count()",
    y=alt.Y('weather:N', title="Weather"),
    color=alt.condition(click, color, alt.value("lightgray")),
).transform_filter(
    brush
).properties(
    width=550,
).add_params(
    click
)

# slap these puppies into a single chart
alt.vconcat(
    points,
    bars,
    data=source,
    title="Seattle Weather: 2012-2015"
).properties(padding=20)
```


## Grammar of Graphics projects
- [Grammar of Graphics](https://link.springer.com/book/10.1007/0-387-28695-0)
- Hadley Wickham's [A Layered Grammar of Graphics](https://vita.had.co.nz/papers/layered-grammar.html)
- [Vega-Lite: A Grammar of Interactive Graphics](https://idl.cs.washington.edu/papers/vega-lite)
- [Altair](https://altair-viz.github.io/) - Python implementation of Vega-Lite
- [Tableu Colorschemes](https://www.tableau.com/blog/colors-upgrade-tableau-10-56782)

## Projects that build on Vega and GoG
- **[Gemini: A Grammar and Recommender System for Animated Transitions in Statistical Graphics](https://idl.cs.washington.edu/papers/gemini)**
    - UW IDL
    - Animated Vega-Lite
- **[Animated Vega-Lite: Unifying Animation with a Grammar of Interactive Graphics](https://vis.csail.mit.edu/pubs/animated-vega-lite/)**
    - MIT CSAIL
    - Animated & interactive Vega-Lite
- **[Probabilistic Grammar of Graphics](https://www.mjskay.com/papers/chi2020-pgog.pdf)**
    - University of Michigan
    - Vega-Lite for probabilistic data representations

## Footnotes
[^1]: O.K. some of the x distributions _are the same_.

[^2]: If you can't create it with D3.jl you're either no longer working on data visualizations or
    you're drawing it by hand at that point.
