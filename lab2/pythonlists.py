list = ["apple", "banana", "cherry"]
print(list)

#list allow using duplicates for example
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#length of list we define by the using function len
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list items can be any of data types(string,int,bool)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

#we can find out the type of list to know it we need to use function type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#we can treat particlular item by using its index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#negative index define that counting will start from end
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#it will return the third, fourth, and fifth item:2 not included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#in this example it dont touch kiwi in such cases when we have only 1 index it wont use it
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#answer will orange,kiwi,melon not including mango

#we can find out that list have or not defined element by using this algorithm
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#we can change the defined item in list by using its index and give it to another element
  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#also we can change particular range of items to another elements
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#also if we point less elements than range the range will be replaces by pointed elements
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#function insert allow us point particular index to our element,other elements will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#function append will add element to the end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#function extend we can use in case if we need to concatenate two lists following by each other
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#by using remove we can delete particular element in list
#If there are more than one item with the specified value, the remove() method removes the first occurance:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop will remove specified index usually if we dont call specifies index pop will delete last one
#del can do the same functions as pop to remove
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#clear will delete all items in list and make it empty
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example:it will print each element separately
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#we also can use loop while but the danger 
#is that while can work infinitely to avoid it we use the specifies statement and will change it inside of loop
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#also we have short way to do it
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#also we can give the conditions and use it to own profit for example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#we can fill list by particular elements by using conditions
newlist = [x for x in range(10) if x < 5]

#we can sort list if list contain strings it will sort it alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#by using this algorithm we can sort list in descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#this example define elements by the condition that who is nearest to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#if we have uppercase letters and lowercase it will sort them by ASCI values
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#inside brackets we can create any conditions
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#also we can just reverse list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#function copy let us dont make efforts by inserting elements to new list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#similar way to copy
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#




