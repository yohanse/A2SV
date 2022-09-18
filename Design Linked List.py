class node:
    
    def __init__(self,val=None,nex=None):
        self.val=val
        self.next=nex
        
        
class MyLinkedList:

    def __init__(self):
        self.root=None
        self.size=0
        self.last=None

    def get(self, index: int) -> int:
        if index>self.size-1:
            return -1
        current=self.root
        for i in range(index):
            current=current.next
        return current.val
        
    def addAtHead(self, val: int) -> None:
        head=self.root
        current=node()
        current.val=val
        if head!=None:
            current.next=head
        else:
            self.last=current
        self.root=current
        self.size=self.size+1
        
    def addAtTail(self, val: int) -> None:
        tail=self.last
        current=node()
        current.val=val
        if tail!=None:
            tail.next=current
        else:
            self.root=current
        self.last=current
        self.size=self.size+1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>=self.size:
            if index==self.size:
                self.addAtTail(val)
        else:
            if index==0:
                self.addAtHead(val)
            else:
                new=node()
                new.val=val
                current=self.root
                for i in range(index):
                    perv=current
                    current=current.next
                perv.next=new
                new.next=current
                self.size=self.size+1
        
    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            current=self.root
            current=current.next
            self.root=current
            self.size=self.size-1
        else:
            if 0<=index<self.size:
                current=self.root
                for i in range(index):
                    perv=current
                    current=current.next
                current=current.next
                perv.next=current
                if index==self.size-1:
                    self.last=perv
                self.size=self.size-1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)