from functools import reduce
def multiply_list(the_list):
    answer=reduce(lambda a,b:a*b,the_list)
    return answer
    
Numbers=[1,2,3,4,5,6]
result=multiply_list(Numbers)
print(result)