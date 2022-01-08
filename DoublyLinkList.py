class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoublyLL:
    def __init__(self):
        self.head=None
    def print_LL_forward(self): # forward or asscending order traversing
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            print()
            print("Forward Order")
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref

    def print_LL_backward(self): # backword or reverse traversing
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            print()
            print("Reverse Order")
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.pref
    def insert_newnode(self,data): # adding new node as Head node
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is Not Empty! ")

    def add_at_begning(self,data):
        new_node=Node(data) # if list is empty
        if self.head is None:
            self.head=new_node
        else:              # if list is not empty
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
        file = open("Captchddl.txt","a")
        file.write(data+" --> ")
        file.close()

    def add_at_end(self,data):    # add at end of linked list
        new_node=Node(data)
        if self.head is None:     # if empty then add at start
            self.head=new_node
        else:                     # traverse list to add at end
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

   # Add node after any Node
    def add_after(self,data,x):      # x is basically node value after which we insert data
        if self.head is None:
            print("Doubly Linked list is empty")
        else:
            # if list is not empty
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Given Node is NOT present in List")
            elif n.nref is None:
                new_node=Node(data)
                n.nref=new_node
                new_node.pref=n
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node

   # Add node before any Node
    def add_before(self,data,x):
       if self.head is None:
           print("Doubly Linked list is empty")
       else:
           # if list is not empty and value add before head or as head
           if self.head.data==x:
               new_node=Node(data)
               self.head.pref=new_node
               new_node.nref=self.head
               self.head=new_node
               return

           n = self.head
           while n is not None:
               if x == n.data:
                   break
               n = n.nref
           if n is None:
               print("Given Node is NOT present in List")
           else:
               new_node=Node(data)
               new_node.nref=n
               new_node.pref=n.pref
               if n.pref is not None:
                   n.pref.nref=new_node
               else:
                   new_node=self.head
                   n.pref=new_node

    def delete_begning(self): # delete from begning
        if self.head is None:
            print("Doubly LL is empty can't delete any Node")
            return
        elif self.head.nref is None:
            self.head=None
            print("DLL is empty after Deleting Head Node")
            return
        else:
            self.head=self.head.nref
            self.head.pref=None

    def delete_from_end(self):
        if self.head is None:
            print("Doubly LL is empty can't delete any Node")
        elif self.head.nref is None:
            self.head=None
            print("DLL is empty after Deleting Head Node")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_By_Value(self,x):
        if self.head is None:
            print("Doubly LL is empty can't delete any Node")
        elif self.head.nref is None: # if only contain one node
            if x == self.head.data:
                self.head=None
            else:
                print("X is not Present in List")
        elif self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
        else:
            n=self.head
            while n.nref is not None:
                if x==n.data:
                    break
                n=n.nref
            if n.nref is not None:
                n.nref.pref=n.pref
                n.pref.nref=n.nref
            else:
                if n.data==x:
                    n.pref.nref=None
                else:
                    print("X is not present in Doubly Linked List")



