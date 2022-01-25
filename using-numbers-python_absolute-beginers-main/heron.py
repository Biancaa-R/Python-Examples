import math
print("this program will help you to calculate the area of any triangle by heron's formula")
a=float(input("enter the value of first side of the triangle"))
b=float(input("enter the value of the second side of the triangle"))
c=float(input("enter the value of the third side of the triangle"))
p=a+b+c
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("the sides of the triangle are ",a,"," ,b, "," ,c)
print("the perimeter of the triangle is",p)
print("the semi perimeter of the triangle is",s)
print("the area of the triangle is",area)

