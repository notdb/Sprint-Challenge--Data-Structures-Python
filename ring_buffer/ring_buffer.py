class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
# when you first initialize a ring buffer you get a list with None * the capacity of the ring buffer. When we need to append an item, we replace one of the nones with the new item. When it's full, we replace the oldest item.

# we can use the capacity to figure out where to put items. We also have a current thing for the item, but I don't think it's necessary

# have a statement to check for none in self.storage
# if a spot is none, insert item there
# need to keep track of the current oldest, we should also increment the current oldest item using the current variable
# once there are no more nones left, when adding something to the ring buffer, add notes

  def append(self, item):
   if None in self.storage:
       for i in range(len(self.storage)):
           if self.storage[i] is None:
               self.storage[i] = item
               return 0
               
  def get(self):
    print(self.storage)

rbuffer = RingBuffer(3)
rbuffer.get()
rbuffer.append('a')
rbuffer.get()
rbuffer.append('b')
rbuffer.get()
rbuffer.append('c')
rbuffer.get()
rbuffer.append('d')
