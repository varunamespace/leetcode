from LinkedList import *


# 2,4,3  5,6,4
n1 = Node(2)
n2 = Node(4)
n3 = Node(3)

n1.next = n2
n2.next = n3
ll1 = LinkedList()

n4 = Node(5)
n5 = Node(6)
n6 = Node(4)
n7 = Node(9)

n4.next = n5
n5.next = n6
n6.next = n7

ll2 = LinkedList()
ll1.head = n1
ll2.head = n4

ll1.printList()
ll2.printList()

ptr1 = n1
ptr2 = n4


s = 0
c = 0
ans = Node(None)
ptr = ans
while ptr1 and ptr2:
    s = (ptr1.val+ptr2.val+c)%10
    c = (ptr1.val+ptr2.val+c)//10
    ptr.next = Node(s)
    ptr = ptr.next
    ptr1 = ptr1.next
    ptr2 = ptr2.next
while ptr1:
    s = (ptr1.val+c)%10
    c = (ptr1.val+c)//10
    ptr.next = Node(s)
    ptr1 = ptr1.next

while ptr2:
    s = (ptr2.val+c)%10
    c = (ptr2.val+c)//10
    ptr.next = Node(s)
    ptr2 = ptr2.next

if c>0:
    ptr.next = Node(c)
    ptr = ptr.next


ansL = LinkedList()
ansL.head = ans
ansL.printList()

