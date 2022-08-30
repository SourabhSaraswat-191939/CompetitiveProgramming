
""" Program to check if a given Binary
Tree is balanced like a Red-Black Tree """
 
# Helper function that allocates a new
# node with the given data and None
# left and right poers.                                
class newNode:
 
    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
# Returns true if given tree is BST.
def isBST(root, mini = None, maxi = None):
 
    # Base condition
    if (root == None) :
        return True
 
    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if mini!=None and root.data<=mini:
        return False
 
    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if maxi!=None and root.data>=maxi:
        return False

    # check recursively for every node.
    left = isBST(root.left, mini, root.data)
    right = isBST(root.right, root.data, maxi)
    return left and right
 
 
# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.right.left = newNode(1)
    root.right.right = newNode(4)
    #root.right.left.left = newNode(40)
    if (isBST(root,None,None)):
        print("Is BST")
    else:
        print("Not a BST")
 