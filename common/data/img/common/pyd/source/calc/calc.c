#include "..\common\common.h"
#include "calc.h"

static PyObject* 
maskAndRight (PyObject *self, PyObject *args) {
  int data = 0;
  int mask = 0;
  int shift = 0;
  if (!PyArg_ParseTuple(args, "iii", &data, &mask, &shift))
    DEBUG_LOG("ARGUMENT IS ERROR!");
  return Py_BuildValue("i",(data & mask)>>shift);
}

static PyObject* 
maskAndLeft (PyObject *self, PyObject *args) {
  int data = 0;
  int mask = 0;
  int shift = 0;
  if (!PyArg_ParseTuple(args, "iii", &data, &mask, &shift))
    DEBUG_LOG("ARGUMENT IS ERROR!");
  return Py_BuildValue("i",((data & mask)<<shift) & 0x1111);
}

static PyObject* 
bitmask (PyObject *self, PyObject *args) {
  int data = 0;
  int mask = 0;
  if (!PyArg_ParseTuple(args, "ii", &data, &mask))
    DEBUG_LOG("ARGUMENT IS ERROR!");
  return Py_BuildValue("i",data|mask);
}

static PyMethodDef calcMethods[] = {
  {"maskAndRight",  (PyCFunction)maskAndRight,  METH_VARARGS | METH_KEYWORDS, "mask AND RightShift"},
  {"maskAndLeft",   (PyCFunction)maskAndLeft,   METH_VARARGS | METH_KEYWORDS, "mask AND LeftShift"},
  {"bitmask",       (PyCFunction)bitmask,       METH_VARARGS | METH_KEYWORDS, "bitmask"},
  {NULL}
};

static struct PyModuleDef calcModule = {
  PyModuleDef_HEAD_INIT,
  "calc",
  NULL,
  -1,
  calcMethods
};

PyMODINIT_FUNC PyInit_calc (void) {
  return PyModule_Create(&calcModule);
}