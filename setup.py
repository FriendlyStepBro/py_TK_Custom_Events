import platform
from setuptools import setup, Extension

# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
    include_dirs = []  # Windows doesn't need special include paths for Tk
else:
    source_file = 'unix_Resize.c'
    if platform.system() == 'Darwin':  # macOS
        include_dirs = ['/opt/X11/include', '/usr/include/tcl', '/usr/include/tk']
        libraries = ['tk', 'tcl', 'X11']
    else:
        include_dirs = ['/usr/include/tcl', '/usr/include/tk']
        libraries = ['tk', 'tcl']

module = Extension(
    'resize_event',
    sources=[source_file],
    include_dirs=include_dirs,  # Add include directories for Tk and X11
    libraries=libraries  # Link with the X11 library on macOS
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)