def temperature(fahrenheit):
    centigrade = ((fahrenheit - 32) * 5) / 9
    return centigrade

temp = int(input("Enter the temperature in Fahrenheit: "))
print(temperature(temp))
