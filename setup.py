import platform
from setuptools import setup, Extension

# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
    include_dirs = []  # Windows doesn't need special include paths for Tk
    libraries = ['tk', 'tcl']
elif platform.system() == 'Darwin':  # macOS
    source_file = 'unix_Resize.c'
    # Include both Tk and X11 headers on macOS
    include_dirs = ['/Library/Frameworks/Tk.framework/Headers', '/opt/X11/include']
    libraries = ['tcl', 'tk', 'X11']
else:  # Linux and others
    source_file = 'unix_Resize.c'
    include_dirs = ['/usr/include/tcl', '/usr/include/tk', '/usr/include/X11']
    libraries = ['tcl', 'tk', 'X11']

module = Extension(
    'resize_event',
    sources=[source_file],
    include_dirs=include_dirs,  # Add include directories for Tk and X11
    libraries=libraries         # Link with Tcl/Tk and X11 libraries
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)