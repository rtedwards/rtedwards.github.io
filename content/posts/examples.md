+++
title = "Example Usage"
date = 1970-01-01

[taxonomies]
tags = ["python", "performance", "pandas"]

[extra]
katex = true
+++

## Code
Let there be Rust! `let var = 10u32;`

```rust
let var = vec!["1", "2", "3"]
```

```jl
var = ["1", "2", "3"]
```

## LaTeX
$e^x$

$ x = 1 + y$

$$ x = 1 + y$$

## Embedding Interactive Maps with Deck.gl
### Local file
Create deck.gl map and download as html.  Save in known directory `static/assets/`
<iframe
    src="/assets/test/geojson_layer.html"
    style="border:0px #ffffff none; border-radius: 10px;"
    name="myiFrame"
    scrolling="no"
    frameborder="1"
    marginheight="0px"
    marginwidth="0px"
    height="600px"
    width="800px"
    allowfullscreen>
</iframe>

### Remote file
- `https://tiiny.host`
<iframe
    src="https://rose-clarey-19.tiiny.site/"
    style="border:0px #ffffff none; border-radius: 10px;"
    name="myiFrame"
    scrolling="no"
    frameborder="1"
    marginheight="0px"
    marginwidth="0px"
    height="600px"
    width="800px"
    allowfullscreen>
</iframe>

### Youtube
<iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/eGUEAvNpz48"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer;
        autoplay;
        clipboard-write;
        encrypted-media;
        gyroscope;
        picture-in-picture"
    allowfullscreen>
</iframe>