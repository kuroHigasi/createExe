#include "..\common\common.h"
#include "action.h"

static PyObject* 
GO_UP_THE_STAIRS (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_GO_UP_THE_STAIRS);
}

static PyObject* 
SEARCH (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_SEARCH);
}

static PyMethodDef actionMethods[] = {
  {"GO_UP_THE_STAIRS",    (PyCFunction)GO_UP_THE_STAIRS,    METH_VARARGS | METH_KEYWORDS, "GO_UP_THE_STAIRS"},
  {"SEARCH",              (PyCFunction)SEARCH,              METH_VARARGS | METH_KEYWORDS, "SEARCH"},
  {NULL}
};

static struct PyModuleDef actionModule = {
  PyModuleDef_HEAD_INIT,
  "action",
  NULL,
  -1,
  actionMethods
};

PyMODINIT_FUNC PyInit_action (void) {
  return PyModule_Create(&actionModule);
}