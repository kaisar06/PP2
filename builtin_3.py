def palindrome(the_string):

    new_string = the_string[::-1]
    
    if new_string == the_string:
        return True
    else:
        return False

checking_string = input("Enter a string: ")

if palindrome(checking_string):
    print("Palindrome")
else:
    print("Not palindrome")
