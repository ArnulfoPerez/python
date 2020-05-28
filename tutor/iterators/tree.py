# Guido's binary tree example.

# A recursive generator that generates Tree labels in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
        yield t.label
        for x in inorder(t.right):
            yield x
# A binary tree class.
class Tree:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right
        
    def __repr__(self, level=0, indent="    "):
        s = level*indent + repr(self.label)
        if self.left:
            s = s + "\n" + self.left.__repr__(level+1, indent)
        if self.right:
            s = s + "\n" + self.right.__repr__(level+1, indent)
        return s
    
    def __iter__(self):
        return inorder(self)

# Create a Tree from a list.
def tree(list):
    n = len(list)
    if n == 0:
        return []
    i = n // 2
    return Tree(list[i], tree(list[:i]), tree(list[i+1:]))
# Show it off: create a tree.
t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for x in t:
    print(' '+x, end='')
print()     
print(t)
