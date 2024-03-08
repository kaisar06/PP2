#set will ignore duplicate values
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#in this case true and 1 will consider as the same element
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#also false and 0
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#function len let find out the length of set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#set elements can be any of data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#also set can have different type of elements
set1 = {"abc", 34, True, 40, "male"}

#type of set
myset = {"apple", "banana", "cherry"}
print(type(myset))

#we can loop through a set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#to add element to a set we have to use add()
  thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#by using update we can unite two sets into one
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#we can remove element from set by using remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#discard() the same as remove
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#pop dont remove last item it remove random item
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#clear make set empty
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#del will work as clear delete set completely
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#union() will work as update() and make the union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#intersection update will remain only those elements which meet in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#intersection will move only elements in both sets to another new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#symmetric will remain only unique elements which meet only in own sets not both
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#

