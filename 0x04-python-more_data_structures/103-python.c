#include <stdio.h>
#include <Python.h>

/**
 * print_python_list -function that prints the list information.
 * @p: Input value
 * Return: void
 */
void print_python_list(PyObject *p)
{
        Py_ssize_t i, size;
        PyObject *item;

        if (!PyList_Check(p))
        {
                printf("Invalid List Object\n");
                return;
        }

        size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++)
        {
                item = PyList_GetItem(p, i);
                printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
}

/**
 * print_python_bytes - function that prints bytes information
 * @p: Input value
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
        Py_ssize_t i, size;
        char *str;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        size = PyBytes_Size(p);
        str = PyBytes_AsString(p);

        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", str);

        printf("  first %ld bytes: ", (size < 10 ? size + 1 : 10));
        for (i = 0; i < size && i < 10; i++)
        {
                printf("%02hhx", str[i]);
                if (i + 1 < size && i + 1 < 10)
                        printf(" ");
        }
        printf("\n");
}

