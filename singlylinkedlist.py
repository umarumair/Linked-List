#Create a class Node with two feilds data and next(Link)
class Node:
    def __init__(self,data=None,next=None):
         self.data=data
         self.next=next
#Create class LinkedList with a head pointer to get starting address og linklist
class LinkedList:
    def __init__(self):
        self.head=None

# Traversal of LinkedList or printing of LinkedList         
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        linkliststr=''
        while itr:
            linkliststr+=str(itr.data)+'-->'
            itr=itr.next
        print(linkliststr)

#Define a function insert_at_begining() with data to insert

    def insert_at_begining(self,data):
        node=Node(data,self.head)        # Creating a Linked List node with self.head poniter as next of new node
        self.head=node                   
      
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
   #Insert the given data at the specified index
    def insert_at_position(self,data,index):
        if index<0 or index>=self.get_length():
            print("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
# Removing an item from begining         
    def remove_at_begining(self):
        self.head=self.head.next
        return
    
# Removing an item from the specified position
    def remove_at_position(self,index):
        if index<0 or index>=self.get_length():
            print("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if(count==index-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
# Removing an item from end     
    def remove_at_end(self):
        itr=self.head
        while itr.next is not None:
            itr.next=itr.next.next
        itr.next=None      
                          
               
linklist=LinkedList()
t='y'
while(t):
    print("The available operations are:1.Insert 2.Remove 3.Traverse 4.Exit")
    c=int(input("Enter your choice"))
    if(c>0 and c<5):
        if(c==1):
            print("The available OPerations are 1.Insert at begining 2.Insert at end 3.Insert at any given position")
            x=int(input("Enter Your Choice"))
            if (x==1):
                n=int(input("Enter value to insert at begining"))
                linklist.insert_at_begining(n)
                linklist.print()
            elif(x==2):
                n=int(input("Enter value to insert at end"))
                linklist.insert_at_end(n)
                linklist.print()
            elif(x==3):
                data=int(input("Enter value to insert"))
                index=int(input("Enter position to insert"))
                linklist.insert_at_position(data,index)
                linklist.print()
        elif(c==2):
            print("The available OPerations are 1.Remove from begining 2. Remove from end 3.Remove from  any given position")
            z=int(input("Enter Your Choice"))
            if (z==1):
                print("After removing first item:")
                linklist.remove_at_begining()
                linklist.print()
            elif(z==2):
                print("After removing last item:")
                linklist.remove_at_end()
                linklist.print()
            elif(z==3):
                index=int(input("Enter position to remove"))
                linklist.remove_at_position(index)
                linklist.print()
        elif(c==3):
            print("The values present are:")
            linklist.print()
        elif(c==4):
            print("Exit")
            break
        t=input("Do you want to continue(y/n)")
    else:
        print("Invalid option")
        t=input("Do you want to continue(y/n)")