thistuple = ("apple", "banana", "cherry")
print(thistuple)

#print the length of tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#we have to use comma if we have only one item in tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple items can be any of data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#it will return that type is tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#we can treat tuple items by using index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#begative indexes the same as list
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#also range the same rules
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#we can change item of tuple by using this operation
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#also add
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#or we can just add two tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#this example as the map in C++ we create the link between elements
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#we can use loop for to iterate through each item
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#also we can use while but dont forget to put i=i+1 inside loop
  thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#we can concatenate and double tuple
  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

