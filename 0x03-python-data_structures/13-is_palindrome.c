#include "lists.h"

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 *
 * @head: singly linked list
 *
 * Return: Integer value.(0 if it is not a palindrome, 1 if it is a palindrome)
 */

int is_palindrome(listint_t **head)
{/* Declaration of Variables */
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
	{/* Check if the list is empty or has only one node */
		return (1); }
	while (fast != NULL && fast->next != NULL)
	{/* Find the middle node of the list */
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp; }
	if (fast != NULL)
	{/* Move the slow pointer to the next node, if condition met */
		slow = slow->next; }
	while (slow != NULL)
	{/* Compare the first half and second half of the list */
		if ((*head)->n != slow->n)
		{
			return (0); } /* Not a palindrome */
		*head = (*head)->next;
		slow = slow->next;
	}
	return (1);  /* Palindrome */
}
