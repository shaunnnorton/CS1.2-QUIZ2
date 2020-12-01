class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.previous = None

class LinkedList:

  def __init__(self,head=None):
    self.head = head
    self.tail = None

  def prepend(self, data):
    new_node = Node(data)
    if self.head is not None:
      self.head.previous = new_node
    new_node.next = self.head
    self.head = new_node

    if self.tail is None:
      self.tail = new_node

  def append(self, data):
    new_node = Node(data)
    new_node.previous = self.tail
    if self.tail is not None:
      self.tail.next = new_node
    self.tail = new_node
    if self.head is None:
      self.head = new_node

  def print_ll(self):
    current = self.head

    while current is not None:
      print(current.data)
      current = current.next

  def clone(self):
    if self.head is None:
      return None
    head = Node(self.head.data)
    head.next = self.head.next
    return head

  def reverse(self):
    current = self.head
    while current is not None:
      next = current.next
      current.next = current.previous
      current.previous = next
      current = next
    head = self.head
    self.head = self.tail
    self.tail = head

class Stack:
  def __init__(self):
    '''Modifies the linked list to behave as a stack'''
    self.top = None
    self.stack = LinkedList()
  
  def append(self, data):
    '''Appends to the top of the stack'''
    self.stack.append(data)

  def remove(self):
    '''Removes from the top of the stack'''
    if self.stack.tail.previous == None:
      return None
    if self.stack.tail != None:
      self.stack.tail = self.stack.tail.previous
      self.stack.tail.next = None

  def read(self):
    '''Reads the top of the stack'''
    return(self.stack.tail.data)