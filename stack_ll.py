#stack using linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head =None

    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False

    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new_node=node(data)
            new_node.next=self.head
            self.head=new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node=self.head
            self.head=self.head.next
            popped_node.next=None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data


    def display(self):
        iternode=self.head
        if self.is_empty:
            print("Stack underflow.")
        else:
            while(iternode!=None):
                print(iternode.data,"-->",end="")
                iternode=iternode.next
                if (iternode!=None):
                    print("-->",end="")
            return

new_stack=stack()
new_stack.push(10)
new_stack.push(12)
new_stack.push(13)
new_stack.push(14)

new_stack.display()

print("Top element is:",new_stack.peek())
new_stack.pop()
new_stack.pop()
new_stack.display()

print("Topn element is:",new_stack.peek())
