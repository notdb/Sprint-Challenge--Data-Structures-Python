class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False
# so we need to find the current head, move backwards until it's None, so move backwards until it's pointing at nothing, build a list while it's doing so, and then make a new list using the current numbers in our current list. so something like assuming 3-2-1 is our current list.
# start at 3, move into temp storage, go to 2, move into temp storage, go to 1, move into temp storage, we see none. start at 3, add 2 to head, add 1 to head
# we can use recursioni to get to the end of the list
# iteration will be faster for me right now
  def reverse_list(self):
      tempList = []
      #print(self.head)
      if self.head is None:
          return 0
      while self.head is not None:
          tempList.append(self.head.value)
          self.head = self.head.get_next()
          print(tempList)
      tempList.reverse()
      for i in range(len(tempList)):
          node = Node(tempList.pop())
          if self.head is not None:
              node.set_next(self.head)
          #print(self.head)
          #print(self.head.value)
          self.head = node
          #print(self.head.value)

newList = LinkedList()
newList.add_to_head(1)
newList.add_to_head(2)
newList.add_to_head(3)
newList.add_to_head(4)
newList.add_to_head(5)
print(newList.head.value)
#print(newList.contains(1))
#print(newList.head.get_next().value)
newList.reverse_list()
print(newList.head.value)
print(newList.head.get_next().value)
print(newList.head.get_next().get_next().value)
