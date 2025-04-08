#include "..\\common\\common.h"
#include "index.h"

static PyObject* 
HOME (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_HOME);
}

static PyObject* 
BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BUTTON);
}

static PyMethodDef indexMethods[] = {
  {"HOME",     (PyCFunction)HOME,     METH_VARARGS | METH_KEYWORDS, "HOME"},
  {"BUTTON",   (PyCFunction)BUTTON,   METH_VARARGS | METH_KEYWORDS, "BUTTON"},
  {NULL}
};

static struct PyModuleDef indexModule = {
  PyModuleDef_HEAD_INIT,
  "index",
  NULL,
  -1,
  indexMethods
};

PyMODINIT_FUNC PyInit_indexHome (void) {
  return PyModule_Create(&indexModule);
}