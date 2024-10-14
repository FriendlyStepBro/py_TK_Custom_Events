import platform
from setuptools import setup, Extension

# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
    include_dirs = []  # Windows doesn't need special include paths for Tk
    libraries = ['tk', 'tcl']
    library_dirs = []  # No additional library directories for Windows
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
    library_dirs=library_dirs   # Add library directories (especially for macOS)
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)