import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# I'm assuming I need an LRU cache to get this to work, but my LRU cache isn't working so I'm going on to reverse the linked list

# An LRU cache should work because we can set it to 10000 spots and pop a name out whenever they're duplicated. The issue with the runtime (n^2) is because of the nested for loops. So we need a way to not have nested for loops. Some sort of caching would help. As of now, taking each name, and multiplying it by 10000 to check for duplicates, since we have 10000 names in list one, it's 10000*10000 (n^2) for names.

# The LRU Cache might help because we can use a dictionary for the faster lookup and store each node of the linked list in the dictionary, and print the max size of the dictionary. The linked list should contain only duplicated. So we'll be building a linked list of 64 names because there's 64 duplicates. 
