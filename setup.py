import platform
from setuptools import setup, Extension

# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
    include_dirs = []  # Windows doesn't need special include paths for Tk
else:
    source_file = 'unix_Resize.c'
    include_dirs = ['/usr/include/tcl', '/usr/include/tk']  # Add correct include paths for Tk

module = Extension(
    'resize_event',
    sources=[source_file],
    include_dirs=include_dirs,  # Add include directories for Tk
    libraries=['tk', 'tcl']
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)