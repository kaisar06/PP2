def histogram(input_list):
    answer_string = ""
    for element in input_list:
        while element > 0:
            answer_string += "*"
            element -= 1
        answer_string += " "
    return answer_string

example_input = input("Enter a list of numbers separated by spaces: ")
the_list = [int(num) for num in example_input.split()]
answer = histogram(the_list)

print("The result is:", answer)
