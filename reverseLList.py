class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
  
class LinkedList:
  def __init__(self):
    self.head = None

  def push(self,data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def reverseList(self):
    prev,curr = None,self.head
    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev

obj = LinkedList()
obj.push(1)
obj.push(2)
obj.push(3)
obj.reverseList()
