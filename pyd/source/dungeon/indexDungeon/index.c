#include "..\\common\\common.h"
#include "index.h"

static PyObject* 
RIGHT (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_RIGHT);
}

static PyObject* 
CENTER (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_CENTER);
}

static PyObject* 
LEFT (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_LEFT);
}

static PyObject* 
FLAME (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_FLAME);
}

static PyObject* 
WALL (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_WALL);
}

static PyObject* 
PLAYER (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_PLAYER);
}

static PyObject* 
PATH (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_PATH);
}

static PyObject* 
BOARD_S (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BOARD_S);
}

static PyObject* 
TEXT3 (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_TEXT3);
}

static PyObject* 
BOARD_M (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BOARD_M);
}

static PyObject* 
TEXT5 (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_TEXT5);
}

static PyObject* 
BUTTON (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BUTTON);
}

static PyObject* 
TEXT6 (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_TEXT6);
}

static PyObject* 
ACTION (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_ACTION);
}

static PyObject* 
ITEM (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_ITEM);
}

static PyObject* 
BOX (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BOX);
}

static PyObject* 
COMPASS (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_COMPASS);
}

static PyObject* 
BOX_TAG (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_BOX_TAG);
}

static PyObject* 
UP_POS (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_UP_POS);
}

static PyObject* 
CENTER_POS (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_CENTER_POS);
}

static PyObject* 
DOWN_POS (PyObject *self, PyObject *args) {
  return Py_BuildValue("i", INDEX_DOWN_POS);
}

static PyMethodDef indexMethods[] = {
  {"RIGHT",     (PyCFunction)RIGHT,     METH_VARARGS | METH_KEYWORDS, "RIGHT"},
  {"CENTER",    (PyCFunction)CENTER,    METH_VARARGS | METH_KEYWORDS, "CENTER"},
  {"LEFT",      (PyCFunction)LEFT,      METH_VARARGS | METH_KEYWORDS, "LEFT"},
  {"FLAME",     (PyCFunction)FLAME,     METH_VARARGS | METH_KEYWORDS, "FLAME"},
  {"WALL",      (PyCFunction)WALL,      METH_VARARGS | METH_KEYWORDS, "WALL"},
  {"PLAYER",    (PyCFunction)PLAYER,    METH_VARARGS | METH_KEYWORDS, "PLAYER"},
  {"PATH",      (PyCFunction)PATH,      METH_VARARGS | METH_KEYWORDS, "PATH"},
  {"BOARD_S",   (PyCFunction)BOARD_S,   METH_VARARGS | METH_KEYWORDS, "BOARD_S"},
  {"TEXT3",     (PyCFunction)TEXT3,     METH_VARARGS | METH_KEYWORDS, "TEXT3"},
  {"BOARD_M",   (PyCFunction)BOARD_M,   METH_VARARGS | METH_KEYWORDS, "BOARD_M"},
  {"TEXT5",     (PyCFunction)TEXT5,     METH_VARARGS | METH_KEYWORDS, "TEXT5"},
  {"BUTTON",    (PyCFunction)BUTTON,    METH_VARARGS | METH_KEYWORDS, "BUTTON"},
  {"TEXT6",     (PyCFunction)TEXT6,     METH_VARARGS | METH_KEYWORDS, "TEXT6"},
  {"ACTION",    (PyCFunction)ACTION,    METH_VARARGS | METH_KEYWORDS, "ACTION"},
  {"ITEM",      (PyCFunction)ITEM,      METH_VARARGS | METH_KEYWORDS, "ITEM"},
  {"BOX",       (PyCFunction)BOX,       METH_VARARGS | METH_KEYWORDS, "BOX"},
  {"COMPASS",   (PyCFunction)COMPASS,   METH_VARARGS | METH_KEYWORDS, "COMPASS"},
  {"BOX_TAG",   (PyCFunction)BOX_TAG,   METH_VARARGS | METH_KEYWORDS, "BOX_TAG"},
  {"UP_POS",    (PyCFunction)UP_POS,    METH_VARARGS | METH_KEYWORDS, "UP_POS"},
  {"CENTER_POS",(PyCFunction)CENTER_POS,METH_VARARGS | METH_KEYWORDS, "CENTER_POS"},
  {"DOWN_POS",  (PyCFunction)DOWN_POS,  METH_VARARGS | METH_KEYWORDS, "DOWN_POS"},
  {NULL}
};

static struct PyModuleDef indexModule = {
  PyModuleDef_HEAD_INIT,
  "index",
  NULL,
  -1,
  indexMethods
};

PyMODINIT_FUNC PyInit_indexDungeon (void) {
  return PyModule_Create(&indexModule);
}