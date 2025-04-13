#include "..\common\common.h"
#include "status.h"

static PyObject* 
HOME (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", STATUS_HOME);
}

static PyObject* 
CONFIG (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", STATUS_CONFIG);
}

static PyObject* 
SAVE (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", STATUS_SAVE);
}

static PyObject* 
DUNGEON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", STATUS_DUNGEON);
}

static PyObject* 
EXIT (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", STATUS_EXIT);
}

static PyObject* 
END (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", STATUS_END);
}

static PyObject* 
existStatus (PyObject *self, PyObject *args) {
  int status = 0;
  if (!PyArg_ParseTuple(args, "i", &status))
    printf("ARGUMENT IS ERROR!");
  if (status < STATUS_COUNT) {
    return Py_BuildValue("O", Py_True);
  }
  return Py_BuildValue("O", Py_False);
}

static PyMethodDef statusMethods[] = {
  {"EXIT",     (PyCFunction)EXIT,     METH_VARARGS | METH_KEYWORDS, "EXIT"},
  {"HOME",     (PyCFunction)HOME,     METH_VARARGS | METH_KEYWORDS, "HOME"},
  {"CONFIG",   (PyCFunction)CONFIG,   METH_VARARGS | METH_KEYWORDS, "CONFIG"},
  {"SAVE",     (PyCFunction)SAVE,     METH_VARARGS | METH_KEYWORDS, "SAVE"},
  {"DUNGEON",  (PyCFunction)DUNGEON,  METH_VARARGS | METH_KEYWORDS, "DUNGEON"},
  {"END",      (PyCFunction)END,      METH_VARARGS | METH_KEYWORDS, "END"},
  {"existStatus",  (PyCFunction)existStatus,  METH_VARARGS | METH_KEYWORDS, "existStatus"},
  {NULL}
};

static struct PyModuleDef statusModule = {
  PyModuleDef_HEAD_INIT,
  "status",
  NULL,
  -1,
  statusMethods
};

PyMODINIT_FUNC PyInit_status (void) {
  return PyModule_Create(&statusModule);
}