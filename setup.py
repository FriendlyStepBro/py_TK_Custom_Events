import platform
from setuptools import setup, Extension
import os

# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
    
    # Use MSYS2 toolchain paths for GCC
    os.environ['CC'] = 'C:/msys64/mingw64/bin/gcc.exe'  # Use MSYS2 GCC compiler
    os.environ['CXX'] = 'C:/msys64/mingw64/bin/g++.exe'  # Use MSYS2 G++
    os.environ['LD'] = 'C:/msys64/mingw64/bin/ld.exe'    # Use MSYS2 linker
    os.environ['AR'] = 'C:/msys64/mingw64/bin/ar.exe'    # Use MSYS2 archiver
    os.environ['RANLIB'] = 'C:/msys64/mingw64/bin/ranlib.exe'  # Use MSYS2 ranlib

    # Include and library paths for Tcl/Tk
    include_dirs = [
        'C:/msys64/mingw64/include'
    ]
    library_dirs = [
        'C:/msys64/mingw64/lib'
    ]
    libraries = ['tcl', 'tk']

elif platform.system() == 'Darwin':  # macOS
    source_file = 'unix_Resize.c'
    include_dirs = ['/Library/Frameworks/Tk.framework/Headers', '/opt/X11/include']
    libraries = ['tcl', 'tk', 'X11']
    library_dirs = ['/opt/X11/lib']

else:  # Linux and others
    source_file = 'unix_Resize.c'
    include_dirs = ['/usr/include/tcl', '/usr/include/tk', '/usr/include/X11']
    libraries = ['tcl', 'tk', 'X11']
    library_dirs = []

module = Extension(
    'resize_event',
    sources=[source_file],
    include_dirs=include_dirs,
    libraries=libraries,
    library_dirs=library_dirs
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)