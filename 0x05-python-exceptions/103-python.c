#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_str;
	PyObject *repr_str, *byte_obj;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n  size: %ld\n", size);

	repr_str = PyObject_Repr(p);
	bytes_str = PyUnicode_AsUTF8(repr_str);

	printf("  trying string: %s\n", bytes_str);

	printf("  first 10 bytes:");
	for (i = 0; i < size && i < 10; ++i)
	{
		byte_obj = PyBytes_GetItem(p, i);
		printf(" %02x", (unsigned char)PyLong_AsLong(byte_obj));
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("[.] float object info\n  value: %lf\n", value);
}
