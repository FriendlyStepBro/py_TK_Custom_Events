from setuptools import setup, Extension

module = Extension('resize_event', sources=['resize_event.c'], libraries=['tk', 'tcl'])

setup(
    name='resize_event',
    version='1.0',
    description='Custom Tkinter resize event',
    ext_modules=[module],
)