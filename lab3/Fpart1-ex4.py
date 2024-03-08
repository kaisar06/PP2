def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
           if num%i==0:
               return False
        return True
def filter_prime(numbers):
    return[num for num in numbers if is_prime(num)]
    
List_of_numbers=input("print numbers which separated by space: ")
Numbers=[int(num) for num in List_of_numbers.split()]

prime_numbers=filter_prime(Numbers)

print("changed list: ",prime_numbers)
