def unique_list(List):
    Unique=[]
    
    for element in List:
        if element not in Unique:
            Unique.append(element)
    return Unique

example_input = input("Enter a list of numbers: ")
example_list = [int(num) for num in example_input.split()]
answer = unique_list(example_list)

print("first list",example_list)
print("unique list",answer)
    