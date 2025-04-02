#include "..\common\common.h"
#include "enemyType.h"

static PyObject* 
DANGER (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", TYPE_DANGER);
}



static PyMethodDef enemyTypeMethods[] = {
  {"DANGER",     (PyCFunction)DANGER,     METH_VARARGS | METH_KEYWORDS, "DANGER"},
  {NULL}
};

static struct PyModuleDef enemyTypeModule = {
  PyModuleDef_HEAD_INIT,
  "enemyType",
  NULL,
  -1,
  enemyTypeMethods
};

PyMODINIT_FUNC PyInit_enemyType (void) {
  return PyModule_Create(&enemyTypeModule);
}