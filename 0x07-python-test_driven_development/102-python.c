#include <Python.h>

/**
 * print_python_string - Prints Python string information.
 *
 * @p: PyObject representing the Python object to be printed.
 */

void print_python_string(PyObject *p)
{
	const char* utf8_str = PyUnicode_AsUTF8(p);

	if (!PyUnicode_Check(p))
	{
		printf("Error: Invalid Python string\n");
		return;
	}
	printf("Python string: %s\n", utf8_str);
}
