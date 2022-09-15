# This is a method to traverse a tree but here we traverse the tree without using any
# memory stack or Auxiliary Space or recursion stack. i.e. S.C-> O(1)  T.C-> O(n)

class newNode: 
    # Construct to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
 
def inOrder(root):
    inorder = []
    curr = root    
    while curr!=None:
        if curr.left == None:
            inorder.append(curr.val)           # 1st time we visit the root.
            curr = curr.right
        else:
            prev = curr.left
            while prev.right is not None and prev.right!=curr:
                prev = prev.right
            if prev.right==None:
                prev.right = curr
                curr = curr.left
            else:                  # 2nd time we visit the root. 
                prev.right = None
                inorder.append(curr.val)
                curr = curr.right

    return inorder
    
def preOrder(root):
    preorder = []
    curr = root    
    while curr!=None:
        if curr.left == None:
            preorder.append(curr.val)           # 1st time we visit the root.
            curr = curr.right
        else:
            prev = curr.left
            while prev.right is not None and prev.right!=curr:
                prev = prev.right
            if prev.right==None:
                prev.right = curr
                preorder.append(curr.val)
                curr = curr.left
            else:                  # 2nd time we visit the root. 
                prev.right = None
                curr = curr.right

    return preorder
    
# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.left.right.right = newNode(6)
    #root.right.left.left = newNode(40)
    print("Inorder ->",inOrder(root))
    print("Preorder ->",preOrder(root))