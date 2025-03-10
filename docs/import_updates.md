# Import Statement Updates for Package Reorganization

This document outlines the changes needed for import statements to reflect the new package structure, where `dreampielib` has been renamed to `dreampie` and moved under the `src` directory.

 

## Types of Import Changes Needed

 

1. **External imports of the package**
   - Change: `from dreampielib.X import Y` → `from dreampie.X import Y`
   - Change: `import dreampielib.X` → `import dreampie.X`

2. **Internal relative imports**
   - Most relative imports like `from . import X` or `from .. import Y` can remain unchanged
   - Adjust any imports that specifically mention `dreampielib`

3. **Entry point imports**
   - Update the main entry point in `dreampie.py` to use the new package name

 

## Files Requiring Updates

 

### Entry Point Files

 

- `dreampie.py`: Update `from dreampielib.gui import main` to `from dreampie.gui import main`

 

### Package Files

 

- Update any imports in the `src/dreampie` directory that reference `dreampielib`
- Pay special attention to:
  - `__init__.py` files in each subpackage
  - Files that import across subpackages

 

### External Files

 

- Any scripts or examples that import from the package

 

## Implementation Approach

 

To minimize risk and ensure backward compatibility:

1. Start with the entry point files
2. Update each subpackage systematically
3. Test after each set of changes
4. Keep track of files modified

 

## Common Import Patterns to Update

 

```python
# Before
from dreampielib import __version__
from dreampielib.common import beep
import dreampielib.subprocess

# After
from dreampie import __version__
from dreampie.common import beep
import dreampie.subprocess
```

 

## Special Cases

 

- The `find_data_dir` function in `gui/__init__.py` contains references to `dreampielib_dir` which should be updated
- Any hardcoded paths that include `dreampielib`
- Any dynamic imports or references to the package name as a string

 

## Testing Strategy

 

After updating imports:

1. Run the application with the new entry point
2. Test basic functionality
3. Check for import errors
4. Verify that all subpackages are properly accessible
