import platform
from setuptools import setup, Extension

# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
    include_dirs = []  # Windows doesn't need special include paths for Tk
    libraries = ['tk', 'tcl']
elif platform.system() == 'Darwin':  # macOS
    source_file = 'unix_Resize.c'
    include_dirs = ['/Library/Frameworks/Tk.framework/Headers']
    libraries = ['tcl', 'tk']
else:  # Linux and others
    source_file = 'unix_Resize.c'
    include_dirs = ['/usr/include/tcl', '/usr/include/tk']
    libraries = ['tcl', 'tk']

module = Extension(
    'resize_event',
    sources=[source_file],
    include_dirs=include_dirs,  # Add include directories for Tk framework on macOS
    libraries=libraries         # Link with Tcl/Tk libraries
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)