def check_for_order(List):
    for i in range(len(List)-2):
        if List[i]==0 and List[i+1]==0 and List[i+2]==7:
            return True

Numbers=input("enter list of numbers: ")
Numbers_list=[int(num) for num in Numbers.split()]
if check_for_order(Numbers_list):
    print("True")
else:
    print("False")
            