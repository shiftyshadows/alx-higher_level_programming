#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject* p)
{/* Declaration of Variable */
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	const char *type;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject*)p)->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject* item = PyList_GetItem(p, i);
		type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, type); }
}
