import math
import time

def square_root(number,milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result


example_number=int(input("Enter a number: "))
example_time = int(input("Enter a milliseconds: "))
answer = square_root(example_number,example_time)
print(f"square root after {example_time} milliseconds: ",answer)