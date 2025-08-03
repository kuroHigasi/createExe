
#include "..\common\common.h"
#include "hit.h"

static PyObject* 
hitJudgeSquare (PyObject *self, PyObject *args) {
  int x = 0;
  int y = 0;
  int size_x = 0;
  int size_y = 0;
  int hit_x = 0;
  int hit_y = 0;
  if (!PyArg_ParseTuple(args, "iiiiii", &x, &y, &size_x, &size_y, &hit_x, &hit_y)) {
    return Py_BuildValue("O", Py_False);    
  }
  if ((x != -1) &&
      (y != -1) &&
      (x <= hit_x && hit_x <= (x+size_x)) &&
      (y <= hit_y && hit_y <= (y+size_y)))
    return Py_BuildValue("O", Py_True);
  return Py_BuildValue("O", Py_False);
}

static PyMethodDef hitJudgeMethods[] = {
  {"hitJudgeSquare", (PyCFunction)hitJudgeSquare, METH_VARARGS | METH_KEYWORDS, "hitJudge(square)"},
  {NULL}
};

static struct PyModuleDef hitJudgeModule = {
  PyModuleDef_HEAD_INIT,
  "hitJudge",
  NULL,
  -1,
  hitJudgeMethods
};

PyMODINIT_FUNC PyInit_hitJudge (void) {
  return PyModule_Create(&hitJudgeModule);
}