from LinkedList import *
ll = LinkedList()
n1,n2,n3,n4 = Node(1),Node(2),Node(3),Node(4)
n1.next = n2
n2.next = n3
n3.next = n4

ll.head = n1
ll.printList()

dummy = Node(None)
ans = dummy
head = n1
ans.next = head

while head and head.next:






"""print(first.data)
print(first.next.data)
print(second.data)
print(second.next.data)"""

#first = second
"""print("after changing the variable")
print(first.data)
print(first.next.data)
print(first.next.next.data)
print(first.next.next.next.data)
print("check")"""

"""ansptr = ans
ans.next = first
while ansptr:
    print(ansptr.data)
    ansptr = ansptr.next


second = first.next
first.next = second.next
second.next = first

first = second
"""