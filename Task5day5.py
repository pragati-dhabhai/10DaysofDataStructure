def remove_duplicates(self):
    pass
  # write your code here
  cur=self.head
  while cur:
      i=cur.next
      while i:
          if(cur.data==index.data):
              temp=i
              i.previous.next=i.next
              if(i.next!=None):
                  i.next.previous = i.previous;
              temp = None
            i = i.next    
     cur = cur.next
                  
      
  
  
