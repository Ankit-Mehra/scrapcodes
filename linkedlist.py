class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = Linkedlist()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next =second
second.next =third


llist.printlist()


