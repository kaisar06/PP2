#if 
a = 33
b = 200
if b > a:
  print("b is greater than a")

#a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error because print has to be a little bit far

#elif is the same as else if in C++
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#also we can use such case
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#we can just use it in one line
  if a > b: print("a is greater than b")

# and use in condition that both condition should be true
  a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or uses when we need to use it when one of statements are true
  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#not the same as a<b
  a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#also we can use if inside ifx = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#