def check_for_similarity(List):
    for i in range(len(List)-1):
        if List[i]==3 and List[i+1]==3:
            return True

Numbers=input("enter list of numbers: ")
Numbers_list=[int(num) for num in Numbers.split()]
if check_for_similarity(Numbers_list):
    print("True")
else:
    print("False")
            