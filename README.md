# Blog

## Resources
- https://quarto.org/
- https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide.html

**theming**
- https://quarto.org/docs/output-formats/html-themes.html
- https://quarto.org/docs/output-formats/html-themes-more.html
- https://quarto.org/docs/output-formats/html-code.html#appearance

## Tooling
- Quarto

## Developing

### Hot Reloading
```bash
quarto preview index.qmd --to html
```

### Render
```bash
quarto render
```

## Deploying

Hosted on **Cloudflare Pages** at https://bear-toes.pages.dev.

The site is rendered locally and the `docs/` output is committed — Cloudflare
does no build of its own. To publish:

```bash
just build          # renders to docs/
git add -A && git commit && git push
```

The project is Git-connected via the Cloudflare GitHub App, so pushing to `main`
triggers a deploy. Note that connecting the repo, and the build settings below,
can only be configured in the Cloudflare dashboard — `wrangler pages project
create` has no flags for them.

| Setting                 | Value     |
| ----------------------- | --------- |
| Project name            | `bear-toes` |
| Framework preset        | None      |
| Build command           | *(empty)* |
| Build output directory  | `docs`    |
| Production branch       | `main`    |

Analytics comes from Cloudflare Web Analytics, enabled per-project under
**Pages → the project → Metrics**. It auto-injects its beacon, so nothing needs
to change in this repo.

### Constraints worth remembering

- Cloudflare Pages rejects any **single file over 25 MiB**. Check with
  `find docs -type f -size +24M` before pushing.
- Limit of 20,000 files per deployment, and 500 builds/month on the free tier.
- If the `*.pages.dev` subdomain ever changes, update `website.site-url` in
  `_quarto.yml` and re-render — it feeds `sitemap.xml`, the RSS feed, and the
  Open Graph tags.