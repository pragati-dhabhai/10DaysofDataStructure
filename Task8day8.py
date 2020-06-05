def is_bst_satisfied(self):
    pass
    return preorder_print()==sorted(preorder_print())
# write your code here
def preorder_print(self, start, traversal):
    if start:
        traversal += list(start.value)
        traversal = self.preorder_print(start.left, traversal)
        traversal = self.preorder_print(start.right, traversal)
    return traversal
