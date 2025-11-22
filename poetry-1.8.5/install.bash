#!/bin/bash

# Install production dependencies only (no dev dependencies)
# This uses the --no-dev flag available in Poetry 1.8.5

echo "Installing production dependencies with Poetry..."
poetry install --no-dev

echo "Installation complete!"
