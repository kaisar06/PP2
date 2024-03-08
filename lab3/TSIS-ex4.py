#import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
        
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    
    def distance(self,second_point):
        dx = self.x - second_point.x
        dy = self.y - second_point.y
        distance=(dx**2+dy**2)**0.5
        return distance

point1=Point(3,4)
point2=Point(6,9)

point1.show()
point2.show()

distance_between=point1.distance(point2)
print(f"Distance between two points: {distance_between}")

point1.move(1,2)
point1.show()