# A simple Python program for traversal of a linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next

def swap(root,i,j):
    if i>j:
        i,j=j,i
    
    ptr = root
    curr=0
    start = Node(-1)
    start.next= root
    prev1=start
    prev2=None
    while curr<=j:
        if curr<i:
            prev1=ptr
            
        if curr<j:
            prev2=ptr

        ptr = ptr.next
        curr+=1

    if i+1!=j:
        prev1.next.next, prev2.next.next = prev2.next.next, prev1.next.next
        prev1.next, prev2.next = prev2.next, prev1.next
    else:
        prev1.next = prev2.next
        prev2.next = prev2.next.next
        prev1.next.next = prev2

    return start.next

# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    #fifth = Node(5)
    #sixth = Node(6)

    llist.head.next = second; # Link first node with second
    second.next = third # Link second node with the third node
    third.next = fourth
    #fourth.next = fifth
    #fifth.next = sixth

    llist.printList()
    llist.head = swap(llist.head,0,1)
    print("----------After Reversing------------")
    llist.printList()
