#we use dict to store values in pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#also we can find out the pair by using his pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#in dictionaries we cannot use duplicates
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#the length of dictionaries
print(len(thisdict))

#also we can have in pair lists it lets us to have multiple choices
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#type()-type of dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#also as index is get
x = thisdict.get("model")

#we can have only keys in lists
x = thisdict.keys()

#the same as keys but values
x = thisdict.values()

#items will return pairs as one element of tuple
x = thisdict.items()

#we can change element of pair by using  specific element
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#it will replace 1964 to 2018
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#such way we create new pair 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#pop will remove pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem remove lastitem
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#clear makes dictionary empty
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#we can treat each element by loop for
for x in thisdict:
  print(x)

#we can get only values or keys by using different statements
  for x in thisdict.values():
  print(x)

  for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

#copy of dictionary
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#dictionary can contain other dictionaries inside
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}