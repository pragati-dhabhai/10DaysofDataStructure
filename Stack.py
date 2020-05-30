class Stack:
    def __init__(self,limit=1000):
        self.top_item=None
        self.size=0
        self.limit=limit
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Stack is empty")
    def push(self,value):
        if self.has_space():
            item=Node(value)
            item.set_next_node(self.top_item)
            self.top_item=item
            self.size+=1
        else:
            print("All out of space!")
    def pop(self):
        if not self.is_empty():
            item_to_remove=self.top_item
            self.top_item = self.top_item.next
            self.size-=1
            return item_to_remove
        else:
            print("Stack is empty")
    def has_space(self):
        return self.limit>self.size
    def is_empty(self):
        return self.size==0
class Node:
    def __init__(self, data):
	    self.data = data
	    self.next = None
    def get_value(self):
	    return self.data

    def set_value(self, data):
	    self.data = data

    def get_next_node(self):
	    return self.next

    def set_next_node(self, next):
	    self.next = next
    
s=Stack()
s.push('A')
print(s.peek())
s.pop()
print(s.peek())


        
        
