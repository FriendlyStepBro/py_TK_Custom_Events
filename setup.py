import platform
from setuptools import setup, Extension
import os

# This script builds the resize_event module, which is a C extension for tkinter events.
# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
    # Use environment variables to get the Tcl/Tk include and lib directories
    include_dirs = [
        os.environ.get('TCL_INCLUDE_DIR', 'C:/Program Files/Tcl/include'),
        os.environ.get('TCL_INCLUDE_DIR', '')  # Fallback if not set
    ]
    library_dirs = [
        os.environ.get('TCL_LIB_DIR', 'C:/Program Files/Tcl/lib'),
        os.environ.get('TCL_LIB_DIR', '')  # Fallback if not set
    ]
    libraries = ['tk', 'tcl']
elif platform.system() == 'Darwin':  # macOS
    source_file = 'unix_Resize.c'
    # Include both Tk and X11 headers on macOS
    include_dirs = ['/Library/Frameworks/Tk.framework/Headers', '/opt/X11/include']
    libraries = ['tcl', 'tk', 'X11']
    library_dirs = ['/opt/X11/lib']  # Add X11 library directory
else:  # Linux and others
    source_file = 'unix_Resize.c'
    include_dirs = ['/usr/include/tcl', '/usr/include/tk', '/usr/include/X11']
    libraries = ['tcl', 'tk', 'X11']
    library_dirs = []  # Default system paths should be enough

module = Extension(
    'resize_event',
    sources=[source_file],
    include_dirs=include_dirs,  # Add include directories for Tk and X11
    libraries=libraries,        # Link with Tcl/Tk and X11 libraries
    library_dirs=library_dirs   # Add library directories
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)