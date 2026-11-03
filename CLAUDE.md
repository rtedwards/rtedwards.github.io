# CLAUDE.md

Guidance for Claude Code when it works in this repository.

## Layout

- `site/` is the Astro site. Posts live in `site/src/content/posts/`.
- `posts/` holds the Quarto posts. They still build with `just build` until they move.
- `scripts/` holds the Python that writes the artifacts the site imports.
- `justfile` lists the recipes. `just setup` installs the tools and dependencies.

## Writing style

Use two spaces after a sentence end. A sentence end is a period, question
mark or exclamation mark. Put the two spaces before the next sentence when
both sentences sit on the same line. A line break inside a wrapped paragraph
does not count. Abbreviations such as "e.g." do not need the second space.

`just lint-prose` checks site prose for this. It reads `site/src` by default.
Pass a path to check other files, for example `just lint-prose posts`. Pass
`--fix` to rewrite single spaces: `just lint-prose --fix site/src`.
