import time
import sys
import hashlib
from binary_search_tree import BinarySearchTree
sys.setrecursionlimit(10001)
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
# so my binary search tree only can compare ints (numbers). What we can do is take the list of names, and turn them into a list of numbers (hash it), and then insert them into my tree. Take the second list of names, hash them the same way, and compare the tree. using contains

# so name.length x 2, insert that
# compare, name2.length x 2
# if yes, add name to thingy.
# this won't work because there are allegedly a lot of names with the exact same length

# it's hard to use a binary search tree for this because ideally we'd have unique keys to compare, unless you want to create a binary search tree of 10000 from 1-10000 and compare every single node when we run through it

# the problem is the names aren't all different lengths. So you can have two names: John and Nohj and they're both the same length of 4 despite being different.

# so we can't turn the names into numbers and then insert them all into the binary tree, and search the tree for a specific number and add the name to the list if it returns true
i = 1
bigTree = BinarySearchTree((0,'f'))
for name_1 in names_1:
     hashedName = ((i, name_1))
     i+= 1
     bigTree.insert(hashedName)
b = 1
for name_2 in names_2:
    hashedName = ((b, name_2))
    b+= 1
    if bigTree.contains(hashedName[0]):
       duplicates.append('true')

end_time = time.time()
print(len(duplicates))
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# I'm assuming I need an LRU cache to get this to work, but my LRU cache isn't working so I'm going on to reverse the linked list

# An LRU cache should work because we can set it to 10000 spots and pop a name out whenever they're duplicated. The issue with the runtime (n^2) is because of the nested for loops. So we need a way to not have nested for loops. Some sort of caching would help. As of now, taking each name, and multiplying it by 10000 to check for duplicates, since we have 10000 names in list one, it's 10000*10000 (n^2) for names.

# The LRU Cache might help because we can use a dictionary for the faster lookup and store each node of the linked list in the dictionary, and print the max size of the dictionary. The linked list should contain only duplicated. So we'll be building a linked list of 64 names because there's 64 duplicates. 
