def volume_of_sphere(Radius):
    volume=((Radius**3)*4*3.14)/3
    return volume
    
radius_of_sphere=int(input("enter the size of radius: "))
print("volume equal to: ",volume_of_sphere(radius_of_sphere))