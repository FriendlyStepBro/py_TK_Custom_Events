#include <Python.h>
#include <tk.h>
#include <stdio.h>

// A callback that will be invoked when the window geometry changes
static void ResizeCallback(ClientData clientData, XEvent *eventPtr) {
    if (eventPtr->type == ConfigureNotify) {
        Tk_Window tkwin = (Tk_Window)clientData;

        int new_width = Tk_Width(tkwin);
        int new_height = Tk_Height(tkwin);

        printf("Window resized: new width = %d, new height = %d\n", new_width, new_height);
    }
}

// Bind the custom resize event to a Tkinter window
static PyObject* bind_resize_event(PyObject* self, PyObject* args) {
    Tk_Window tkwin;
    Tk_Window window;

    if (!PyArg_ParseTuple(args, "O&", Tk_Window, &window)) {
        return NULL;
    }

    Tk_CreateEventHandler(window, StructureNotifyMask, ResizeCallback, (ClientData)window);

    Py_RETURN_NONE;
}

// Method definition for the Python module
static PyMethodDef ResizeMethods[] = {
    {"bind_resize_event", bind_resize_event, METH_VARARGS, "Bind the custom <Resize> event"},
    {NULL, NULL, 0, NULL}
};

// Module definition for Python
static struct PyModuleDef resizemodule = {
    PyModuleDef_HEAD_INIT,
    "resize_event",
    "C extension for Tkinter to handle custom resize events",
    -1,
    ResizeMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_resize_event(void) {
    return PyModule_Create(&resizemodule);
}
