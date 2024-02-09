def palindrome(input_string):
    check="".join(reversed(input_string))
 
    if check==input_string:
        return True
    else:
        return False

example_string=input("print a string: ")
if palindrome(example_string):
    print("True")
else:
    print("False")
    