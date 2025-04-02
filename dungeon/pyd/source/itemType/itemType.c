#include "..\common\common.h"
#include "itemType.h"

static PyObject* 
COMPASS (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", TYPE_COMPASS);
}

static PyObject* 
RADER (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", TYPE_RADER);
}

static PyObject* 
getText (PyObject *self, PyObject *args) {
    int index = 0;
    if (!PyArg_ParseTuple(args, "i", &index)) {
        return Py_BuildValue("s", "");
    }
    switch (index) {
        case TYPE_COMPASS:
            return Py_BuildValue("s", TEXT_COMPASS);
        case TYPE_RADER:
            return Py_BuildValue("s", TEXT_RADER);
        default:
            return Py_BuildValue("s", "");
    }
}


static PyMethodDef itemTypeMethods[] = {
  {"COMPASS",     (PyCFunction)COMPASS,     METH_VARARGS | METH_KEYWORDS, "COMPASS"},
  {"RADER",       (PyCFunction)RADER,       METH_VARARGS | METH_KEYWORDS, "RADER"},
  {"getText",     (PyCFunction)getText,     METH_VARARGS | METH_KEYWORDS, "getText"},
  {NULL}
};

static struct PyModuleDef itemTypeModule = {
  PyModuleDef_HEAD_INIT,
  "itemType",
  NULL,
  -1,
  itemTypeMethods
};

PyMODINIT_FUNC PyInit_itemType (void) {
  return PyModule_Create(&itemTypeModule);
}