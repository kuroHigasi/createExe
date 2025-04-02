#include "..\common\common.h"
#include "num.h"

static PyObject* 
BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_COMMON_BUTTON);
}

static PyObject* 
CONFIG (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_CONFIG_CONFIG);
}

static PyObject* 
CONFIG_BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_CONFIG_BUTTON);
}

static PyObject* 
CONFIG_SET_BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_CONFIG_SETBUTTON);
}

static PyObject* 
END (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_END_END);
}

static PyObject* 
HOME (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_HOME_HOME);
}

static PyObject* 
SAVE (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_SAVE_SAVE);
}

static PyObject* 
SAVE_LIST (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_SAVE_LIST);
}

static PyObject* 
SAVE_BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", IMG_NUM_SAVE_BUTTON);
}

static PyMethodDef numMethods[] = {
  {"BUTTON",            (PyCFunction)BUTTON,            METH_VARARGS | METH_KEYWORDS, "BUTTON"},
  {"CONFIG",            (PyCFunction)CONFIG,            METH_VARARGS | METH_KEYWORDS, "CONFIG"},
  {"CONFIG_BUTTON",     (PyCFunction)CONFIG_BUTTON,     METH_VARARGS | METH_KEYWORDS, "CONFIG_BUTTON"},
  {"CONFIG_SET_BUTTON", (PyCFunction)CONFIG_SET_BUTTON, METH_VARARGS | METH_KEYWORDS, "CONFIG_SET_BUTTON"},
  {"END",               (PyCFunction)END,               METH_VARARGS | METH_KEYWORDS, "END"},
  {"HOME",              (PyCFunction)HOME,              METH_VARARGS | METH_KEYWORDS, "HOME"},
  {"SAVE",              (PyCFunction)SAVE,              METH_VARARGS | METH_KEYWORDS, "SAVE"},
  {"SAVE_LIST",         (PyCFunction)SAVE_LIST,         METH_VARARGS | METH_KEYWORDS, "SAVE_LIST"},
  {"SAVE_BUTTON",       (PyCFunction)SAVE_BUTTON,       METH_VARARGS | METH_KEYWORDS, "SAVE_BUTTON"},
  {NULL}
};

static struct PyModuleDef numModule = {
  PyModuleDef_HEAD_INIT,
  "num",
  NULL,
  -1,
  numMethods
};

PyMODINIT_FUNC PyInit_num (void) {
  return PyModule_Create(&numModule);
}