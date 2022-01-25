#program to compare 3 numbrs and give the value of the largest number and the least number to the user
x=y=z=0
x=float(input("Enter the value of the first number"))
y=float(input("Enter the value of the second number"))
z=float(input("enter the value of the third number"))
max=x
if y>=max:
    max=y
if z>=max:
    max=z
print("the largest number is",max)

min=x
if y<=min:
    min=y
if z<=min:
    min=z
print("the smallest number is",min)


