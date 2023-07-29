+++
title = "Uses for Python's Walrus Operator"
date = 2023-03-25
description = "TOD"
summary = "How to use the walrus operator for error handling in python"

[taxonomies]
tags = ["python"]

[extra]
katex = true

+++

[Python 3.8](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions) introduced
**assignment expressions** with the new syntax `:=`, a.k.a the **walrus operator**.
The walrus operator assigns a value to a variable and returns that variable as part of a
larger expression.

It's been out for a few years at this point (at the time of writing Python 3.12 is around the corner) and
I've found some joy in how it's helped elegantly shorten some parts of my code.  Here are the ways I've
made use of the walrus operator.

## Error Handling
**TODO: More warning handling I guess** The walrus operator can help reduce repetition and make error handling with `None` a bit more streamlined.

```python
x = func()
if not x:
    logger.error("Error message")
    return
```

```python
if not x := func():
    logger.error("Error message")
    return
```

**TODO: Add example/anecdote from experience**.  It may seem trivial but becomes more apparent when handling many such cases.  For example, when parsing
inputs and performing validation.  Not shown is an outer level function that would ask for a new input.

```python
if not x := validate_x(inputs):
    logger.error("ValueError: could not validate 'x' from input")
    return

if not y := validate_y(inputs):
    logger.error("ValueError: could not validate 'y' from input")
    return

if not z := validate_y(inputs):
    logger.error("ValueError: could not validate 'z' from input")
    return
```

## Comprehensions
Let's say we wanted to create a list of results from expensive function call but only results that aren't `None`.
With a list comprehension, the expensive function would need to be called twice.  Not ideal.
```python
y = [expensive_function(i) if expensive_function(i) for i in range(0, 10)]
```

Of course, you could use a normal loop but it's a fair bit more verbose.
```python
y = []
for a in range(0, 10):
    x = expensive_function(i)
    if x == 0:
        y.append(x)
```

The walrus operator plops to the rescue here and allows us to use a list comprehension.
```python
y = [x if (x := expensive_function(i)) for i in range(0, 10)]
```
This also applies to dictionary comprehensions.
```python
y = {
    i: expensive_function(i) if expensive_function(i) for i in range(0, 10)
}
```

```python
y = {
    i: x if (x := expensive_function(i)) for i in range(0, 10)
}
```

## Do While Loops

A do-while loop was proposed in [PEP 315](https://peps.python.org/pep-0315/) but was rejected for not
providing a significant improvement over using an infinite loop and condition to break out of the loop early.

```python
while True:
    x = f(a, b) # setup code
    if not x:   # condition
        break
    # loop body
```

A shortened version of do-while loop may also be accomplished by having setup code execute once before the loop
and moving the condition into a while loop.  The problem with this version is that it's error-prone; `x = f(a, b)`
is duplicated and if it changes during a refactor both instances need to be changed.
```python
x = f(a, b) # setup code
while x:    # condition
    x = f(a, b)
    # loop body
```

With the walrus operator this becomes simply
```python
while x := f(a, b): # setup code and condition
    # loop body
```
