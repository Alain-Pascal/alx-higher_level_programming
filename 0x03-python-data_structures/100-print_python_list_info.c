#include "lists.h"
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic infor about Python lists
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = 0;
	int num = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject
						*)p)->allocated);

		while (num < size)
		{
			printf("Element %d: %s\n", num,
					Py_TYPE(PyList_GetItem(p,
							num))->tp_name);
			num++;
		}
	}
}
