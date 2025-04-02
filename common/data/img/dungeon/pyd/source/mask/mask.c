#include "..\common\common.h"
#include "mask.h"

static PyObject* 
L (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_L);
}

static PyObject* 
C (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_C);
}

static PyObject* 
R (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_R);
}

static PyObject* 
LU (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_LU);
}

static PyObject* 
LC (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_LC);
}

static PyObject* 
LD (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_LD);
}

static PyObject* 
RU (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_RU);
}

static PyObject* 
RC (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_RC);
}

static PyObject* 
RD (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", DEFINE_MASK_RD);
}

static PyMethodDef maskMethods[] = {
  {"L",        (PyCFunction)L,        METH_VARARGS | METH_KEYWORDS, "MASK_L"},
  {"C",        (PyCFunction)C,        METH_VARARGS | METH_KEYWORDS, "MASK_C"},
  {"R",        (PyCFunction)R,        METH_VARARGS | METH_KEYWORDS, "MASK_R"},
  {"LU",        (PyCFunction)LU,        METH_VARARGS | METH_KEYWORDS, "MASK_LU"},
  {"LC",        (PyCFunction)LC,        METH_VARARGS | METH_KEYWORDS, "MASK_LC"},
  {"LD",        (PyCFunction)LD,        METH_VARARGS | METH_KEYWORDS, "MASK_LD"},
  {"RU",        (PyCFunction)RU,        METH_VARARGS | METH_KEYWORDS, "MASK_RU"},
  {"RC",        (PyCFunction)RC,        METH_VARARGS | METH_KEYWORDS, "MASK_RC"},
  {"RD",        (PyCFunction)RD,        METH_VARARGS | METH_KEYWORDS, "MASK_RD"},
  {NULL}
};

static struct PyModuleDef maskModule = {
  PyModuleDef_HEAD_INIT,
  "mask",
  NULL,
  -1,
  maskMethods
};

PyMODINIT_FUNC PyInit_mask (void) {
  return PyModule_Create(&maskModule);
}