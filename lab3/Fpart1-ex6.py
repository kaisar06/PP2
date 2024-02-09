def reverse_sentence(sentence):
    words=sentence.split()
    reversed_sentence=' '.join(reversed(words))
    
    return reversed_sentence
    
input_string=input("enter a string: ")
new_sentence=reverse_sentence(input_string)

print("new reversed string is: ",new_sentence)