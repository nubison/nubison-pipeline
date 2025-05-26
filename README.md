# Nubison Pipeline

This project is a SDK for integrating ML pipeline to Nubison.

## Installation

```bash
# Install using uv
uv sync

# Or install using pip
pip install -e .
```

## Dependency Management

```bash
# Install dependencies
uv sync

# Install with development dependencies
uv pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests with tox (multiple Python versions)
tox
```

## Basic Usage

```python
from nubison_pipeline import NubisonPipeline

# Initialize the pipeline
pipeline = NubisonPipeline(name="my-pipeline")

# Run the pipeline
result = pipeline.run(data_path="path/to/data")
print(result)
```

## Note

- This project uses `uv` for dependency management
- Python 3.9 or higher is required
- Package versions are limited to those uploaded before November 26, 2024
