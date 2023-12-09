from LinkedList import *

n1 = Node(1)
n2 = Node(2)
#n3 = Node(1)

n1.next = n2
#n2.next = n3

ll = LinkedList()
ll.head = n1
ll.printList()

t = n1
r = n1
while t and r and r.next:
    t = t.next
    r = r.next.next

temp =None
while t:
    after = t.next
    t.next = temp
    temp = t
    t = after
check = n1
while t:
    if(check.data!=t.val):
        print(False)
    t = t.next
    check = check.next
print(True)