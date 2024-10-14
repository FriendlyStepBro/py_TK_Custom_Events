#include <tk.h>
#include <Python.h>

/* Function to bind the resize event */
static PyObject* bind_resize_event(PyObject* self, PyObject* args) {
    Tk_Window tkwin;
    const char *window_name;
    Tcl_Interp *interp;
    
    if (!PyArg_ParseTuple(args, "s", &window_name)) {
        return NULL;
    }

    /* Retrieve the Tcl interpreter (assuming it's been initialized) */
    interp = Tk_MainWindow(interp);  // Ensure you have access to the correct interpreter

    /* Convert the window name to a Tk_Window */
    tkwin = Tk_NameToWindow(interp, window_name, Tk_MainWindow(interp));
    if (tkwin == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to convert window name to Tk_Window.");
        return NULL;
    }

    /* Now, you can work with the tkwin as a valid Tk_Window */
    
    Py_RETURN_NONE;
}

/* Method definition */
static PyMethodDef ResizeMethods[] = {
    {"bind_resize_event", bind_resize_event, METH_VARARGS, "Bind a resize event"},
    {NULL, NULL, 0, NULL}
};

/* Module definition */
static struct PyModuleDef resize_eventmodule = {
    PyModuleDef_HEAD_INIT,
    "resize_event",
    NULL,
    -1,
    ResizeMethods
};

/* Module initialization function */
PyMODINIT_FUNC PyInit_resize_event(void) {
    return PyModule_Create(&resize_eventmodule);
}