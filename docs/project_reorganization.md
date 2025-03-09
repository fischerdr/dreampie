# DreamPie Project Reorganization Guide

## Overview

This document outlines the recommended changes to reorganize the DreamPie project structure according to modern Python best practices. The goal is to improve maintainability and follow standard conventions without altering the core functionality.

## Current Structure Analysis

The current project structure has several characteristics:

- Uses a mix of older `setup.py` and newer `pyproject.toml` for packaging
- Main package is `dreampielib` with subpackages for different components
- Entry points are defined in both the root directory and within the package
- Data files are stored within the package structure

## Recommended Directory Structure

```text
dreampie/
├── src/
│   └── dreampie/           # Rename from dreampielib to match project name
│       ├── __init__.py     # Move version info here
│       ├── common/         # Keep existing subpackage
│       ├── gui/            # Keep existing subpackage
│       ├── subprocess/     # Keep existing subpackage
│       └── data/           # Keep existing data directory
├── tests/                  # Dedicated test directory
├── docs/                   # Expanded documentation
├── scripts/                # Utility scripts like create-shortcuts.py
└── examples/               # Example usage (if applicable)
```

## Specific Changes Required

### 1. Package Reorganization

- **Rename Package**: Change `dreampielib` to `dreampie` to match project name
- **Source Directory**: Move package under `src/` directory for modern Python packaging
- **Version Information**: Keep version information in the package `__init__.py`

### 2. Entry Point Standardization

- Remove standalone `dreampie` and `dreampie.py` files
- Define all entry points in `pyproject.toml` using the `console_scripts` mechanism
- Update entry point references to reflect new package structure

### 3. Configuration Updates

- Keep `pyproject.toml` as the primary configuration file
- Remove `setup.py` in favor of modern packaging
- Update `MANIFEST.in` to reflect the new structure
- Move build-related scripts to a `build` directory

### 4. Test Organization

- Create dedicated `tests` directory at the project root
- Organize tests to mirror package structure
- Ensure all tests can be run with pytest

### 5. Documentation Enhancement

- Expand documentation in `docs/` directory
- Add installation, usage, and development guides
- Include API documentation
- Update README.md with clear installation and usage instructions

## Implementation Steps

1. Create the new directory structure
2. Move files to their new locations:

   ```text
   mkdir -p src/dreampie
   mv dreampielib/* src/dreampie/
   ```

3. Update package imports to reflect new structure
4. Update configuration files:
   - Update `pyproject.toml` with new package paths
   - Update package data references
5. Test the reorganized package structure
6. Update documentation to reflect changes

## Benefits of Reorganization

- **Improved Discoverability**: Standard structure makes it easier for new contributors
- **Better Packaging**: Modern packaging practices improve distribution
- **Clearer Separation**: Clear separation between package code and supporting files
- **Maintainability**: Easier to maintain and extend the codebase
- **Testing**: Dedicated test directory improves test organization

## Compatibility Considerations

- Ensure backward compatibility for existing users
- Consider providing migration guidance for users of previous versions
- Maintain existing functionality while improving structure

This reorganization follows modern Python packaging standards while maintaining the existing functionality and minimizing code changes. The focus is purely on structural improvements without altering the core functionality of the application.
