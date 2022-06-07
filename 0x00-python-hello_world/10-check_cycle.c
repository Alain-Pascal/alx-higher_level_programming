#include "lists.h"

/**
 * check_cycle - checks if a linked list is a cycle
 * @list: list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *d = list;
	listint_t *r = list;

	if (list == NULL)
		return (0);

	while (d && d->next)
	{
		r = r->next;
		d = d->next->next;

		if (r == d)
			return (1);
	}

	return (0);
}
