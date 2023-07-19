#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyObject_HasAttrString(p, "__iter__")) {
        printf("Invalid Python list\n");
        return;
    }

    size = PyObject_Length(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the list = %ld\n", size);

    for (i = 0; i < size; i++) {
        item = PySequence_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        Py_DECREF(item);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("Invalid Python bytes object\n");
        return;
    }

    size = PyObject_Length(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);

    if (size > 10)
        size = 10;

    str = PyUnicode_AsUTF8AndSize(p, NULL);

    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02x", (unsigned char)str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}
