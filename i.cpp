// C++ implementation to find the sum of
// nodes of the Linked List
#include <bits/stdc++.h>
using namespace std;

/* A Linked list node */
struct Node {
	int data;
	struct Node* next;
};

// function to insert a node at the
// beginning of the linked list
void push(struct Node** head_ref, int new_data)
{
	/* allocate node */
	struct Node* new_node = new Node;

	/* put in the data */
	new_node->data = new_data;

	/* link the old list to the new node */
	new_node->next = (*head_ref);

	/* move the head to point to the new node */
	(*head_ref) = new_node;
}

// function to recursively find the sum of
// nodes of the given linked list
void sumOfNodes(struct Node* head, int* sum)
{
	// if head = NULL
	if (!head)
		return;

	// recursively traverse the remaining nodes
	sumOfNodes(head->next, sum);

	// accumulate sum
	*sum = *sum + head->data;
}

// utility function to find the sum of nodes
int sumOfNodesUtil(struct Node* head)
{

	int sum = 0;

	// find the sum of nodes
	sumOfNodes(head, &sum);

	// required sum
	return sum;
}

// Driver program to test above
int main()
{
	struct Node* head = NULL;

	// create linked list 7->6->8->4->1
	push(&head, 7);
	push(&head, 6);
	push(&head, 8);
	push(&head, 4);
	push(&head, 1);

	cout << "Sum of nodes = "
		<< sumOfNodesUtil(head);
	return 0;
}
