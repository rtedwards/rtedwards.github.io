export QUARTO_PYTHON := justfile_directory() / ".venv/bin/python"

# List available recipes
default:
    @just --list

# Preview the site locally
preview:
    quarto preview index.qmd --to html

# Render the full site
build:
    quarto render --to html

# Preview including draft posts
preview-drafts:
    quarto preview index.qmd --to html --profile draft

# Clean Quarto build artifacts
clean:
    rm -rf _site _freeze .quarto docs

# Install everything needed to build and preview the site (run `mise install` first if mise is new here)
setup:
    mise install
    uv sync
    cd site && npm ci
    @command -v quarto >/dev/null || echo "note: quarto not found. Only the legacy Quarto build needs it: https://quarto.org/docs/get-started/"

# Sync Python dependencies with uv
sync:
    uv sync

# Check prose for two spaces after sentence ends (pass paths, or --fix to rewrite)
lint-prose *args:
    python3 scripts/check_prose.py {{args}}

# Run the Python behind the posts and write the artifacts the Astro site imports
site-artifacts:
    .venv/bin/python scripts/build_artifacts.py

# Build the Astro site into site/dist (regenerates artifacts first)
site-build: site-artifacts
    cd site && npm run build

# Preview the Astro site locally (regenerates artifacts first)
site-dev: site-artifacts
    cd site && npm run dev
