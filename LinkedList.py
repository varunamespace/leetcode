class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        res = ""
        while temp:
            res = res + (str(temp.data) + " ")
            temp = temp.next
        print(res)

    def add(self,val,ind):
        if ind == 0:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
            return
        def findprev(ind):
            find = self.head
            count = 1
            while(count<ind):
                find = find.next
                count = count + 1
            return find
        previous = findprev(ind)
        nextnode = previous.next
        toinsert = Node(val)
        toinsert.next = nextnode
        previous.next = toinsert

    def delenode(self,key):
        temp = self.head
        if temp is None:
            return
        if(temp.data == key):
            self.head = temp.next
            temp = None
            return
        while(temp.next.data!=key):
            temp = temp.next
        todel = temp.next
        temp.next = todel.next
        todel.next = None
