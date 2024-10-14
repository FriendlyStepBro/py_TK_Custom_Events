import platform
from setuptools import setup, Extension

# Detect the platform
if platform.system() == 'Windows':
    source_file = 'win_Resize.c'
else:
    source_file = 'unix_Resize.c'

module = Extension(
    'resize_event',
    sources=[source_file],  # Use the correct source file based on OS
    libraries=['tk', 'tcl']
)

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)
