#include "lists.h"
/**
 * check_cycle - detect a loop in a linked list
 * @list: a pointer to a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1step = list, *ptr2step = list;

	/*traverse linked list using two pointers*/
	while (ptr1step && ptr2step && ptr2step->next)
	{
		/*move pointer ptr1step by one*/
		ptr1step = ptr1step->next;
		/*move pointer ptr2step by two*/
		ptr1step = ptr2step->next->next;
		/*pointers meet at the same node then there is a loop*/
		if (ptr1step == ptr2step)
			return (1);
	}
	/*pointers do not meet then linked list doesnt have a loop*/
	return (0);
}
