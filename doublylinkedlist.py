#Create a class Node with three fields data,prev(Link) next(Link)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
#Create class LinkedList with a head pointer to get starting address og linklist
class LinkedList:
    def __init__(self):
        self.head=None
#Define a function insert_at_begining() with data to insert
    def insertAtBeginning(self,data):
        if self.head is None:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node

    def insertAtEnd(self,data):
        if self.head is None:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        else:
            new_node=Node(data)
            itr=self.head
            while itr.next is not None:
                itr=itr.next
            itr.next=new_node
            new_node.prev=itr
#Insert the given data at the specified index
    def insertAtPosition(self,data,position):
        count=0
        itr=self.head
        while itr.next is not None:
            if count==(position-1):
                new_node=Node(data)
                new_node.next=itr.next
                new_node.prev=itr
                itr.next=new_node
                new_node.next.prev=new_node
            itr=itr.next
            count=count+1
# Removing an item from begining
    def deleteAtBeginning(self):
        itr=self.head
        if itr.next is None:
            self.head=None
        else:
            self.head=itr.next
            self.head.prev=None

    def deleteAtEnd(self):
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        itr.prev.next=None
# Removing an item from the specified position
    def deleteAtPosition(self,position):
        itr=self.head
        count=0
        while itr.next is not None:
            if count==(position-1):
                itr.next=itr.next.next
                itr.next.prev=itr
            itr=itr.next
            count=count+1
# Traversal of LinkedList or printing of LinkedList
    def printList(self):
        itr=self.head
        while(itr):
            print(str(itr.data)+"=> ",end="")
            itr=itr.next
            

linklist=LinkedList()
ch='y'
while(ch=='y'):
    print("Double Linked List Operations")
    print("1.Insert 2.Remove 3.Traverse 4.Exit")
    c=int(input("Enter your choice: "))
    if (c>0 and c<5):
        if(c==1):
            print("1.Insert At Beginning 2.Insert At End 3.Insert at any position")
            x=int(input("Enter your choice"))
            if (x==1):
                n=int(input("Enter Value At Beginning"))
                linklist.insertAtBeginning(n)
                linklist.printList()
            elif (x==2):
                n=int(input("Enter Value At End"))
                linklist.insertAtEnd(n)
                linklist.printList()
            elif (x==3):
                data=int(input("Enter Value"))
                index=int(input("Enter Position"))
                linklist.insertAtPosition(data,index)
                linklist.printList()
        elif(c==2):
            print("1.Delete At Beginning 2.Delete At End 3.Delete at any position")
            y=int(input("Enter your choice"))
            if (y==1):
                linklist.deleteAtBeginning()
                linklist.printList()
            elif (y==2):
                linklist.deleteAtEnd()
                linklist.printList()
            elif (y==3):
                index=int(input("Enter Position"))
                linklist.deleteAtPosition(index)
                linklist.printList()
        elif(c==3):
            print("Double Linked List Is:")
            linklist.printList()
        elif(c==4):
            print("EXIT")
            break
        ch=input("\ndo you want to continue(y/n)")
    else:
        print("Invalid Option")
        ch=input("\ndo you want to continue(y/n)")