def gram_to_ounces(gramms):
    ounces = 28.3495231 * gramms
    return ounces

gramm = int(input("Enter the amount in grams: "))
print(gram_to_ounces(gramm))
