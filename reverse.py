from LinkedList import *
ll = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

ll.head = n1
ll.printList()

head = n1
temp = None
while head:
    after = head.next
    head.next = temp
    temp = head
    head = after

revl = LinkedList()
revl.head = n4
revl.printList()