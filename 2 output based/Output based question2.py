#code snippet 1
#Output based question
def my_func(var1=100,var2=200):
    var1+=10
    var2=var2-10
    return var1+var2
print(my_func(50),my_func())

#code snippet 2
def changer(P,Q=10):
    P=P/Q
    Q=P%Q
    print(P,"#",Q)
    return P
A=200
B=20
A=changer(A,B)
print(A,"$",B)
B=changer(B)
print(A,"$",B)
