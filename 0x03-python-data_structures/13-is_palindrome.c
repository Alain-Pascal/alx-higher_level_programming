#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if it is a plindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int tab[2048], i = 0, j = 0;

	if (*head)
	{
		while (current)
		{
			tab[i] = current->n;
			current = current->next;
			i += 1;
		}

		while (j < i / 2)
		{
			if (tab[j] == tab[i - j - 1])
				j++;
			else
				return (0);
		}
	}

	return (1);
}
