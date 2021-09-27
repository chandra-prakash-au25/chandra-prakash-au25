class Node:
   def __init__(self,data):
      self.data=data
      self.next=None
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
head.next.next.next.next.next=Node(7)
head.next.next.next.next.next.next=Node(8)
curr=head
head2=None
head3=None
while curr.next!=None:
   if curr.data%2==0:
      if head2==None:
         head2=Node(curr.data)
         curr2=head2
      else:
         curr2.next=Node(curr.data)
         curr2=curr2.next
   else:
      if head3==None:
         head3=Node(curr.data)
         curr3=head3
      else:
         curr3.next=Node(curr.data)
         curr3=curr3.next
   curr=curr.next
curr2.next=head3
def printf(head):
   a=head
   if a==None:
      return
   else:
      print(a.data)
      printf(a.next)
printf(head3)
