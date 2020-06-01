    def is_circular_linked_list(self, input_list):
        pass
        cur=input_list.self.head
        while cur:
            cur=cur.next
            if cur == self.head:
                break
        if cur==self.head:
            print('Circular linked list')
        else
        print('Not a circular linked list')
