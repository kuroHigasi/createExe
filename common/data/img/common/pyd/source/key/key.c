#include "..\common\common.h"

static PyObject* 
key (PyObject *self, PyObject *args) {
    return Py_BuildValue("s", "x14mxeexa3xa0x8dx87xb5:xeb^ZGRx86x8c");
}

static PyMethodDef keyMethods[] = {
    {"key",  (PyCFunction)key,  METH_VARARGS | METH_KEYWORDS, "key"},
    {NULL}
};
  
static struct PyModuleDef keyModule = {
    PyModuleDef_HEAD_INIT,
    "key",
    NULL,
    -1,
    keyMethods
};
  
PyMODINIT_FUNC PyInit_key (void) {
    return PyModule_Create(&keyModule);
}