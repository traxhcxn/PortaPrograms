#stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
    def display(self):
        iternode = self.head
        if self.is_empty():
            print("Stack Underflow")
        else:
            while(iternode != None):
                print(iternode.data, end = "")
                iternode = iternode.next
                if(iternode != None):
                    print(" -> ", end = "")
        return
stack = Stack()
stack.push(10)
stack.push(12)
stack.push(13)
stack.push(14)
stack.display()
print("\nTop element is ", stack.peek())
stack.pop()
stack.pop()
stack.display()
print("\nTop element is ", stack.peek())
