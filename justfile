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

# Sync Python dependencies with uv
sync:
    uv sync
