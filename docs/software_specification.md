# DreamPie Software Specification

## Project Overview

DreamPie is an interactive Python shell (REPL - Read-Eval-Print Loop) designed to be reliable, feature-rich, and enjoyable to use. It provides an enhanced interactive environment for Python development with features like code completion, syntax highlighting, command history, and separate input/output areas. DreamPie supports multiple Python interpreters (including CPython, Jython, IronPython, and PyPy) and runs on Windows, Linux, and macOS platforms.

The application aims to provide a more powerful alternative to the standard Python shell with a focus on developer productivity and an improved user experience. It combines the immediate feedback of an interactive shell with IDE-like features in a GTK-based graphical interface.

## Architecture Summary

DreamPie follows a client-server architecture where:

1. **Main Process (Client)**: A GTK-based GUI application that handles user interaction, display, and command management.
2. **Subprocess (Server)**: A Python interpreter process that executes code and returns results to the main process.

These components communicate via a socket connection, with the main process sending commands and the subprocess executing them and returning results. This separation allows DreamPie to remain responsive even when executing long-running operations and provides isolation between the GUI and execution environments.

The application is structured into several key packages:
- `dreampielib.gui`: Contains the GUI components and main application logic
- `dreampielib.subprocess`: Manages the Python interpreter subprocess
- `dreampielib.common`: Shared utilities used by both the GUI and subprocess

## Module Breakdown

### Main Components

#### GUI Module (`dreampielib.gui`)
- **DreamPie** (in `__init__.py`): Main application class that initializes the GUI, manages the subprocess, and coordinates between different components.
- **Output**: Manages the output display area, handling different types of output (stdout, stderr, results).
- **Folding**: Provides code folding functionality to hide/show sections of code.
- **Selection**: Handles text selection in both the output and input areas.
- **History**: Manages command history, allowing navigation through previous commands.
- **HistPersist**: Handles saving and loading of session history to/from files.
- **Autocomplete**: Provides code completion functionality.
- **CallTips**: Displays function signature and documentation.
- **Autoparen**: Automatically adds parentheses after function names.
- **SubprocessHandler**: Manages communication with the Python interpreter subprocess.

#### Subprocess Module (`dreampielib.subprocess`)
- **Subprocess**: Main class that runs the Python interpreter, executes code, and communicates results back to the GUI.
- **GuiHandler** and implementations (GtkHandler, GIHandler, Qt4Handler, TkHandler): Handle GUI events from different GUI toolkits.
- **Various utility functions**: For code compilation, execution, and result formatting.

### Key Functions and Responsibilities

#### GUI Components
- **DreamPie.execute_source()**: Executes the code in the source buffer.
- **DreamPie.call_subp()**: Makes RPC calls to the subprocess.
- **DreamPie.configure()**: Applies configuration settings.
- **DreamPie.complete_attributes()**, **complete_firstlevels()**, etc.: Provide code completion functionality.

#### Subprocess Components
- **Subprocess.loop()**: Main loop that receives commands and sends results.
- **Subprocess.execute()**: Executes Python code and formats results.
- **Subprocess.complete_attributes()**, **complete_firstlevels()**, etc.: Provide code completion data.
- **user_code()**: Context manager for running user code with proper SIGINT handling.

## Data Flow

1. **Input**: User enters Python code in the source buffer (input area).
2. **Command Execution**:
   - User triggers execution (Enter or Ctrl+Enter)
   - Code is sent to the subprocess via socket
   - Subprocess compiles and executes the code
   - Results, stdout, stderr are captured
   - Data is sent back to the main process

3. **Output Display**:
   - Main process receives execution results
   - Output is formatted and displayed in the output area
   - Different types of output (stdout, stderr, results) are displayed with different styling

4. **Code Completion**:
   - User triggers completion (period, tab, or explicit request)
   - Request is sent to subprocess
   - Subprocess analyzes the code context and returns completion options
   - Main process displays completion options in a popup

5. **History Management**:
   - Commands are stored in history
   - Results can be stored in a result history (configurable size)
   - History can be saved to and loaded from files

## Concurrency and Performance Considerations

1. **Process Separation**: The use of separate processes for the GUI and code execution ensures that long-running or blocking operations don't freeze the interface.

2. **SIGINT Handling**: Special handling of SIGINT (Ctrl+C) signals to allow interrupting running code without terminating the application.

3. **GUI Event Processing**: The subprocess includes handlers for various GUI toolkits to process GUI events while executing code, preventing the interface from becoming unresponsive.

4. **Asynchronous Communication**: Communication between the main process and subprocess is handled asynchronously, with timeouts to prevent blocking.

5. **Result Size Limitation**: Large result objects are truncated to prevent performance issues when displaying or transmitting them.

## Dependencies

### External Libraries
- **PyGTK**: For the graphical user interface
- **GTKSourceView**: For syntax highlighting and advanced text editing
- **Various Python Standard Library modules**: socket, os, sys, traceback, etc.

### Optional Dependencies
- Support for various GUI toolkits in the subprocess (GTK, Qt, Tkinter)
- Support for special handling of matplotlib in interactive/non-interactive modes

## Assumptions and Constraints

1. **Python Version Compatibility**: Designed primarily for Python 2.6/2.7, with some compatibility considerations for Python 3.x.

2. **Platform Considerations**:
   - Windows: Special handling for console windows and PyGTK loading
   - Linux: Special handling for SIGINT signals
   - macOS: Special handling for menu accelerators

3. **Interpreter Flexibility**: Designed to work with various Python interpreters (CPython, Jython, IronPython, PyPy) with different capabilities and limitations.

4. **Display Constraints**:
   - Result size limitations to prevent performance issues
   - Special handling for large objects in code completion

5. **Security Considerations**:
   - Execution happens in a separate process, providing some isolation
   - No explicit sandboxing of executed code

6. **Design Choices**:
   - Separation of input and output areas for clarity
   - History persistence for session continuity
   - Code folding for managing long outputs
   - Syntax highlighting and code completion for productivity
