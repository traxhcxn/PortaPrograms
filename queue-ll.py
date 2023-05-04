class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class queue:
    def __init__(self):
        self.head=None
        
    def is_empty(self):
        if self.head is None:
            print("Queue is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
                
    def enqueue(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
            
    def dequeue(self):
        if self.head is None:
            print("Queue Underflow")
        else:
            self.head=self.head.next
            
    def peek(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print('Top element is:',self.head.data)
            
q=queue()
q.enqueue(30)
q.enqueue(20)
q.enqueue(40)
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(10)
q.is_empty()
q.peek()
