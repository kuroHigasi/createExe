#include "..\\common\\common.h"
#include "index.h"

static PyObject* 
CONFIG (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_CONFIG);
}

static PyObject* 
CONFIG_BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_CONFIG_BUTTON);
}

static PyObject* 
BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BUTTON);
}

static PyObject* 
SET_BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_SET_BUTTON);
}

static PyMethodDef indexMethods[] = {
  {"CONFIG",          (PyCFunction)CONFIG,        METH_VARARGS | METH_KEYWORDS, "CONFIG"},
  {"CONFIG_BUTTON",   (PyCFunction)CONFIG_BUTTON, METH_VARARGS | METH_KEYWORDS, "CONFIG_BUTTON"},
  {"BUTTON",          (PyCFunction)BUTTON,        METH_VARARGS | METH_KEYWORDS, "BUTTON"},
  {"SET_BUTTON",      (PyCFunction)SET_BUTTON,    METH_VARARGS | METH_KEYWORDS, "SET_BUTTON"},
  {NULL}
};

static struct PyModuleDef indexModule = {
  PyModuleDef_HEAD_INIT,
  "index",
  NULL,
  -1,
  indexMethods
};

PyMODINIT_FUNC PyInit_indexConfig (void) {
  return PyModule_Create(&indexModule);
}