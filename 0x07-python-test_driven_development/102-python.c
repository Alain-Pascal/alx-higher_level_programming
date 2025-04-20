#include <Python.h>
#include <stdio.h>

/**
 * print_python_string: prints info about Python strings
 * @p: A PyObject representing a Python string
 */

void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	Py_ssize_t length;
	const char *value;
	int is_compact_ascii;

	length = PyUnicode_GET_LENGTH(p);
	is_compact_ascii = PyUnicode_IS_COMPACT_ASCII(p);

	printf("[.] string object info\n");
	if (is_compact_ascii)
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", length);

	value = PyUnicode_AsUTF8(p);
	if (value)
		printf("  value: %s\n", value);
	else
	{
		Py_UNICODE *unicode_value = PyUnicode_AsUnicode(p);

		if (unicode_value)
		{
			printf("  value: ");
			for (Py_ssize_t i = 0; i < length; ++i)
				printf("%lc", unicode_value[i]);
			printf("\n");
		}
		else
		{
			printf("  [ERROR] Failed to decode string\n");
		}
	}
}
