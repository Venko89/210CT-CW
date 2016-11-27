class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
    #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
    #the function which deletes the node from the tail
      def delete(self,n):
          if n.prev != None:
              n.prev.next = n.next
          else:
              self.head = n.next
          if n.next != None:
              n.next.prev = n.prev
          else:
              self.tail = n.prev
    #displays the result of the DLL
      def display(self):
          values=[]
          n=self.head
          while n!=None:
                values.append(str(n.value))
                n = n.next
          print ("List: ",",".join(values))
if __name__ == '__main__':
      l = List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      #Command to delete a specific node through delete function
      l.delete(Node(6))
      #to display the new DLL list through display function
      l.display()
