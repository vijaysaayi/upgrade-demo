# My Simple App

A simple Poetry example demonstrating the `--no-dev` argument (available in Poetry 1.8.5).

## Installation

### Install production dependencies only (no dev tools):
```bash
poetry install --no-dev
```

### Install all dependencies (including dev tools):
```bash
poetry install
```

## Usage

Run the application:
```bash
poetry run python my_simple_app/__init__.py
```

## Key Commands with --no-dev

- `poetry install --no-dev` - Install only production dependencies
- `poetry update --no-dev` - Update only production dependencies
- `poetry export -f requirements.txt --output requirements.txt --no-dev` - Export without dev dependencies

## Dependencies

**Production:**
- requests - HTTP library
- pandas - Data analysis library

**Development:**
- pytest - Testing framework
- black - Code formatter
- flake8 - Linter
