def size_(self, node):
    pass
# write your code here
    if start is None:
    return 
    queue = Queue()
    queue.enqueue(start)
    traversal = ""
    while len(queue) > 0:
        traversal += str(queue.peek()) + "-"
        node = queue.dequeue()
    if node.left:
      queue.enqueue(node.left)
    if node.right:
      queue.enqueue(node.right)
    return len(traversal)
