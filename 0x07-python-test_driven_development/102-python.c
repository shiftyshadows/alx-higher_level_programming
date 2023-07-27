#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints Python string information.
 *
 * @p: PyObject representing the Python object to be printed.
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	const char *str = PyUnicode_AsUTF8AndSize(p, &len);

	if (!PyUnicode_Check(p))
	{
		printf("Error: Invalid string object\n");
		return;
	}
	if (str == NULL)
	{
	printf("Error: Unable to decode the string\n");
	return;
	}
	printf("String data:\n");
	printf("  Length: %zd\n", len);
	printf("  Value: %s\n", str);
}
