import os
A = ord('A')
for i in range(A, A + 26):
    k = chr(i) + ".txt"
    file_name = os.path.join(os.getcwd(), k)
    with open(file_name, 'w') as file:
        file.write(file_name)