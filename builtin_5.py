def true_tuple(example):
    return all(example)

the_tuple=(True,True,True)
if true_tuple(the_tuple):
    print("all true")
else:
    print("not all true")