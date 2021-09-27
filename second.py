# linked list even 
class Node :
   def __init__(self,data):
      self.data=data
      self.next=None
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
head.next.next.next.next.next=Node(4)
def printf(head):
   curr=head
   if curr==None:
      return
   else:
      print(curr.data)
      curr=curr.next
curr=head
pre=None
Next=head.next
head2=head
while head2.data%2!=0:
   head2=head2.next
print(head2.data)
end=head
while end.next==None:
   end=end.next
nend=end
while curr!=end:
   if curr.data%2==0:
      pre=curr
      curr=curr.next
      Next=Next.next
   else:
      k=curr.data
      print(k)
      nend.next=Node(k)
      nend=nend.next
      curr=Next
      Next=Next.next
      pre.next=curr
print(head2.data)
print(nend.data)
printf(head2)
