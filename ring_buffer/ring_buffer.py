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
               if i == 0:
                   self.current = item
                   self.storage[i] = item
                   return 0
               else:
                   self.storage[i] = item
                   return 0
   else:
       for i in range(len(self.storage)):
           print(self.storage[i])
           print(self.current)
           if self.storage[i] == self.current:
               self.storage[i] = item
               if i+1 == len(self.storage):
                   self.current = self.storage[0]
               else:
                   self.current = self.storage[i+1]
               return 0
  def get(self):
      # apparently we can't display lists with none in the ring buffer so we have to write some code to chop off the none when displaying it if there's none in the list.
      # essentially
      fakeList = []
      if None in self.storage:
          for i in range(len(self.storage)):
              if self.storage[i] is not None:
                  fakeList.append(self.storage[i])
          return fakeList
      else:
          return self.storage

