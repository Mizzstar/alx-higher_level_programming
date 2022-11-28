#include <stdlib.h>
#includ "lists.h"

/**
 * check_cycle - checks if a singly-linked list contains a cycle.
 * @list: a singly-linked list.
 *
 * Return: if there is no cycle - 0.
 * if there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	here = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}