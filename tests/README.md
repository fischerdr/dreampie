# DreamPie Tests

This directory contains tests for the DreamPie project. The test structure mirrors the package structure.

## Test Organization

Tests are organized to mirror the package structure:

```text
tests/
├── test_common/        # Tests for dreampie.common
├── test_gui/           # Tests for dreampie.gui
├── test_subprocess/    # Tests for dreampie.subprocess
└── conftest.py         # Shared pytest fixtures
```

## Running Tests

To run the tests, use pytest:

```text
pytest
```

Or to run a specific test file:

```text
pytest tests/test_specific_module.py
```

## Writing Tests

When adding new tests:

1. Follow the package structure
2. Name test files with `test_` prefix
3. Name test functions with `test_` prefix
4. Use pytest fixtures for shared setup
