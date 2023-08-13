+++
title = "Example Usage"
date = 1970-01-01
draft = true

[taxonomies]
tags = ["python", "performance", "pandas"]

[extra]
katex = true
+++

## Markdown
&nbsp; - 1 space \
&ensp; - 2 spaces \
&emsp; - 4 spaces \

## Code
Let there be Rust! `let var = 10u32;`

```rust
let var = vec!["1", "2", "3"]
```

```julia
var = ["1", "2", "3"]
```

```python
var = ["1", "2", "3"]
```

```golang
var = ["1", "2", "3"]
```

```C
var uint_8 = 1;
```

```Cpp
var uint_8 = 1;
```

```bash
pip list | grep jupyter
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

### Remote File (Google Drive)
https://drive.google.com/file/d/[image_id]/view?usp=sharing
https://drive.google.com/uc?export=view&id=[image_id]

<p style="text-align:center;">
    <img
        src="https://drive.google.com/uc?export=view&id=1pzaupboVK3_OIxad_gBTBDoLeAJrP2tB"
        style="border:0px #ffffff none; border-radius: 10px;"
        alt="animated vega-lite"
    >
</p>

### Remote file (Tiny Host)
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

# Header 1
This is header 1.

## Header 2
This is header 2.

### Header 3
This is header 3.

#### Header 4
This is header 4.

##### Header 5
This is header 5.

###### Header 6
This is header 6.
