#include <Python.h>
#include <stdio.h>

/**
 * Prints basic information about a Python list.
 *
 * @param p The Python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * Prints basic information about a Python bytes object.
 *
 * @param p The Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;
	PyObject *repr;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	repr = PyObject_Repr(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes: ", size + 1 < 10 ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i + 1 < size + 1 && i + 1 < 10)
		{
			printf(" ");
		}
	}
	printf("\n");
	printf("  python repr: %s\n", PyUnicode_AsUTF8(repr));
}