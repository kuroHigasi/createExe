#include "..\\common\\common.h"
#include "index.h"

static PyObject* 
SAVE (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_SAVE);
}

static PyObject* 
BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BUTTON);
}

static PyObject* 
LIST (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_LIST);
}

static PyObject* 
SAVE_BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_SAVE_BUTTON);
}

static PyMethodDef indexMethods[] = {
  {"SAVE",        (PyCFunction)SAVE,            METH_VARARGS | METH_KEYWORDS, "SAVE"},
  {"BUTTON",      (PyCFunction)BUTTON,          METH_VARARGS | METH_KEYWORDS, "BUTTON"},
  {"LIST",        (PyCFunction)LIST,            METH_VARARGS | METH_KEYWORDS, "LIST"},
  {"SAVE_BUTTON", (PyCFunction)SAVE_BUTTON,     METH_VARARGS | METH_KEYWORDS, "SAVE_BUTTON"},
  {NULL}
};

static struct PyModuleDef indexModule = {
  PyModuleDef_HEAD_INIT,
  "index",
  NULL,
  -1,
  indexMethods
};

PyMODINIT_FUNC PyInit_indexSave (void) {
  return PyModule_Create(&indexModule);
}