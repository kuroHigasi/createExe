#include "..\common\common.h"
#include "index.h"

static PyObject* 
END (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_END);
}

static PyObject* 
BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BUTTON);
}

static PyMethodDef indexMethods[] = {
  {"END",      (PyCFunction)END,      METH_VARARGS | METH_KEYWORDS, "END"},
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

PyMODINIT_FUNC PyInit_index (void) {
  return PyModule_Create(&indexModule);
}