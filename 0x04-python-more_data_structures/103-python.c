#include <Python.h>
#include <stdio.h>

/**
 * Prints basic information about a Python list.
 *
 * @param p The Python list object.
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    size = PyObject_Length(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = item->ob_type->tp_name;
        printf("Element %zd: %s\n", i, typeName);
    }
}

/**
 * Prints basic information about a Python bytes object.
 *
 * @param p The Python bytes object.
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyObject_Length(p);
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %zd bytes: ", size < 10 ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char)str[i]);
        if (i + 1 < size && i + 1 < 10) {
            printf(" ");
        }
    }
    printf("\n");
}
