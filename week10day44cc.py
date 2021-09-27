class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
def nodear(head):
    if head==None:
        return
    pre=None
    curr=head
    next=head.next
    while(head.data%2!=0):
        head=head.next
    curr1=curr
    while curr1.next!=None:
        curr1=curr1.next
    end=curr1
    while(curr!=end):
        if curr.data%2==0:
            pre=curr
            curr=curr.next
        else:
            pre=curr.next
            pre.next=curr.next.next
            curr1.next=curr
            curr1=curr1.next
            curr=pre.next
    return head
k=nodear(head)
def pri(head):
    cu=head
    while(cu!=None):
        print(cu.data)
        cu=cu.next
pri(k)   