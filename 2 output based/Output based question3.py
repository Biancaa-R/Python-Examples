#code snippet 1
list1=[10,15,20,25,30 ]
list1.insert(3,4)
list1.insert(2,3)
print(list1[-5])

#code snippet 2
def hello(x=120,y=234):
    x+=y
    y-=x
    print(x,"#",y)
    return (x+y)
a=hello()
print(a)
b=hello(9,23)
print("<",b,">")
c=hello(2345,4567)
#Note even when we just assign the function value the print statement will get executed

#code snippet 3

