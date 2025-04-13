#include "..\\common\\common.h"
#include "eventType.h"

static PyObject* 
INFO (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", EVENT_INFO);
}

static PyObject* 
WARNING (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", EVENT_WARNING);
}

static PyObject* 
FLAVOR (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", EVENT_FLAVOR);
}

static PyObject* 
ITEM (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", EVENT_ITEM);
}

static PyObject* 
getText (PyObject *self, PyObject *args) {
    int index = 0;
    if (!PyArg_ParseTuple(args, "i", &index)) {
        return Py_BuildValue("s", EVENT_FLAVOR_TEXT);
    }
    switch (index) {
        case EVENT_INFO:
        case EVENT_ITEM:
            return Py_BuildValue("s", EVENT_INFO_TEXT);
        case EVENT_WARNING:
            return Py_BuildValue("s", EVENT_WARNING_TEXT);
        case EVENT_FLAVOR:
        default:
            return Py_BuildValue("s", EVENT_FLAVOR_TEXT);
    }
}

static PyMethodDef eventTypeMethods[] = {
  {"INFO",      (PyCFunction)INFO,      METH_VARARGS | METH_KEYWORDS, "INFO"},
  {"WARNING",   (PyCFunction)WARNING,   METH_VARARGS | METH_KEYWORDS, "WARNING"},
  {"FLAVOR",    (PyCFunction)FLAVOR,    METH_VARARGS | METH_KEYWORDS, "FLAVOR"},
  {"ITEM",      (PyCFunction)ITEM,      METH_VARARGS | METH_KEYWORDS, "ITEM"},
  {"getText",   (PyCFunction)getText,   METH_VARARGS | METH_KEYWORDS, "getText"},
  {NULL}
};

static struct PyModuleDef eventTypeModule = {
  PyModuleDef_HEAD_INIT,
  "eventType",
  NULL,
  -1,
  eventTypeMethods
};

PyMODINIT_FUNC PyInit_typeEvent (void) {
  return PyModule_Create(&eventTypeModule);
}