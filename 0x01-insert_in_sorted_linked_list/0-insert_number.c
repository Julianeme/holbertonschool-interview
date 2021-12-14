#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: a double pointer to the head of the linked list
 * @number: the int value stored in the node
 * Return: the address of the node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node = *head;

	new_node = NULL;
	temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!*head)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	else if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		while (temp->next)
		{
			if (number < temp->next->n)
			{
				new_node->next = temp->next;
				temp->next = new_node;
				return (new_node);
			}
			temp = temp->next;
		}
		temp->next = new_node;
		new_node->next = NULL;
	}
	return (new_node);
}
