#include "..\common\common.h"
#include "save.h"

static PyObject* 
SAVE_HEAD (PyObject *self, PyObject *args) {
    int index = 0;
    if (!PyArg_ParseTuple(args, "i", &index)) {
        DEBUG_LOG("ARGUMENT IS ERROR!");
    }
    switch (index) {
        case 0:
            return Py_BuildValue("s", HEAD_SAVE_0);
        case 1:
            return Py_BuildValue("s", HEAD_SAVE_1);
        case 2:
        default:
            return Py_BuildValue("s", HEAD_SAVE_2);
    }
}

static PyObject* 
SAVE_TAIL (PyObject *self, PyObject *args) {
    int index = 0;
    if (!PyArg_ParseTuple(args, "i", &index)) {
        DEBUG_LOG("ARGUMENT IS ERROR!");
    }
    switch (index) {
        case 0:
            return Py_BuildValue("s", TAIL_SAVE_0);
        case 1:
            return Py_BuildValue("s", TAIL_SAVE_1);
        case 2:
        default:
            return Py_BuildValue("s", TAIL_SAVE_2);
    }
}

static PyObject* 
CONF_HEAD (PyObject *self, PyObject *args) {
    return Py_BuildValue("s", HEAD_CONF);
}

static PyObject* 
CONF_TAIL (PyObject *self, PyObject *args) {
    return Py_BuildValue("s", TAIL_CONF);
}

static PyObject* 
PASS (PyObject *self, PyObject *args) {
    return Py_BuildValue("s", SAVE_PASS);
}

static PyObject* 
FOLDER (PyObject *self, PyObject *args) {
    return Py_BuildValue("s", SAVE_FOLDER);
}

static PyMethodDef saveMethods[] = {
  {"SAVE_HEAD", (PyCFunction)SAVE_HEAD, METH_VARARGS | METH_KEYWORDS, "SAVE_HEAD"},
  {"SAVE_TAIL", (PyCFunction)SAVE_TAIL, METH_VARARGS | METH_KEYWORDS, "SAVE_TAIL"},
  {"CONF_HEAD", (PyCFunction)CONF_HEAD, METH_VARARGS | METH_KEYWORDS, "CONF_HEAD"},
  {"CONF_TAIL", (PyCFunction)CONF_TAIL, METH_VARARGS | METH_KEYWORDS, "CONF_TAIL"},
  {"PASS",      (PyCFunction)PASS,      METH_VARARGS | METH_KEYWORDS, "PASS"},
  {"FOLDER",    (PyCFunction)FOLDER,    METH_VARARGS | METH_KEYWORDS, "FOLDER"},
  {NULL}
};

static struct PyModuleDef savemodule = {
  PyModuleDef_HEAD_INIT,
  "save",
  NULL,
  -1,
  saveMethods
};

PyMODINIT_FUNC PyInit_save (void) {
  return PyModule_Create(&savemodule);
}