x = "Hello"
y = 15

print(bool(x))#true
print(bool(y))#true

bool("abc")#true
bool(123)#true
bool(["apple", "cherry", "banana"])#true

#values which return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#checking value to integer or not
x = 200
print(isinstance(x, int))



