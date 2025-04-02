#include "..\common\common.h"
#include "way.h"

static PyObject* 
UP (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", WAY_UP);
}

static PyObject* 
isUp (PyObject *self, PyObject *args) {
  int way = 0;
  if (!PyArg_ParseTuple(args, "i", &way))
    DEBUG_LOG("ARGUMENT IS ERROR!");
  if (way==WAY_UP) {
    return Py_BuildValue("O", Py_True);
  }
  return Py_BuildValue("O", Py_False);
}

static PyObject* 
RIGHT (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", WAY_RIGHT);
}

static PyObject* 
isRight (PyObject *self, PyObject *args) {
  int way = 0;
  if (!PyArg_ParseTuple(args, "i", &way))
    DEBUG_LOG("ARGUMENT IS ERROR!");
  if (way==WAY_RIGHT) {
    return Py_BuildValue("O", Py_True);
  }
  return Py_BuildValue("O", Py_False);
}

static PyObject* 
LEFT (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", WAY_LEFT);
}

static PyObject* 
isLeft (PyObject *self, PyObject *args) {
  int way = 0;
  if (!PyArg_ParseTuple(args, "i", &way))
    DEBUG_LOG("ARGUMENT IS ERROR!");
  if (way==WAY_LEFT) {
    return Py_BuildValue("O", Py_True);
  }
  return Py_BuildValue("O", Py_False);
}

static PyObject* 
DOWN (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", WAY_DOWN);
}

static PyObject* 
isDown (PyObject *self, PyObject *args) {
  int way = 0;
  if (!PyArg_ParseTuple(args, "i", &way))
    DEBUG_LOG("ARGUMENT IS ERROR!");
  if (way==WAY_DOWN) {
    return Py_BuildValue("O", Py_True);
  }
  return Py_BuildValue("O", Py_False);
}

static PyMethodDef indexMethods[] = {
  {"UP",        (PyCFunction)UP,        METH_VARARGS | METH_KEYWORDS, "UP"},
  {"isUp",      (PyCFunction)isUp,      METH_VARARGS | METH_KEYWORDS, "isUp"},
  {"RIGHT",     (PyCFunction)RIGHT,     METH_VARARGS | METH_KEYWORDS, "RIGHT"},
  {"isRight",   (PyCFunction)isRight,   METH_VARARGS | METH_KEYWORDS, "isRight"},
  {"LEFT",      (PyCFunction)LEFT,      METH_VARARGS | METH_KEYWORDS, "LEFT"},
  {"isLeft",    (PyCFunction)isLeft,    METH_VARARGS | METH_KEYWORDS, "isLeft"},
  {"DOWN",      (PyCFunction)DOWN,      METH_VARARGS | METH_KEYWORDS, "DOWN"},
  {"isDown",    (PyCFunction)isDown,    METH_VARARGS | METH_KEYWORDS, "isDown"},
  {NULL}
};

static struct PyModuleDef wayModule = {
  PyModuleDef_HEAD_INIT,
  "way",
  NULL,
  -1,
  indexMethods
};

PyMODINIT_FUNC PyInit_way (void) {
  return PyModule_Create(&wayModule);
}