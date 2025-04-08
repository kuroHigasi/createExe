#include "..\common\common.h"
#include "pass.h"

static PyObject* 
getImgPass (PyObject *self, PyObject *args) {
  char * obj_c = NULL;
  char * case_c = NULL;
  char * pos_c = NULL;
  int patarn_i = 0;
  char patarn_c[100];
  char return_c[100];
  if (!PyArg_ParseTuple(args, "ssi", &case_c, &pos_c, &patarn_i))
    printf("ARGUMENT IS ERROR!");
  sprintf(patarn_c, "%d", patarn_i);
  sprintf(return_c, PASS_DATA_IMG ,case_c, pos_c, pos_c, patarn_c);
  return Py_BuildValue("s", return_c);
}

static PyObject* 
getFontPass (PyObject *self, PyObject *args) {
  char * obj_c = NULL;
  char * font = NULL;
  char return_c[100];
  if (!PyArg_ParseTuple(args, "s", &font))
    printf("ARGUMENT IS ERROR!");
  sprintf(return_c, PASS_DATA_FONT , font);
  return Py_BuildValue("s", return_c);
}

static PyMethodDef createPassMethods[] = {
  {"getImgPass",   (PyCFunction)getImgPass,   METH_VARARGS | METH_KEYWORDS, "getPass(img)"},
  {"getFontPass",  (PyCFunction)getFontPass,  METH_VARARGS | METH_KEYWORDS, "getPass(font)"},
  {NULL}
};

static struct PyModuleDef createPassmodule = {
  PyModuleDef_HEAD_INIT,
  "createPass",
  NULL,
  -1,
  createPassMethods
};

PyMODINIT_FUNC PyInit_createPass (void) {
  return PyModule_Create(&createPassmodule);
}