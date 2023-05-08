#include "lists.h"

/**
 * check_cycle - checks for cycles in a singly linked list.
 * @list: pointer to head 
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle 
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL)
	{
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}
