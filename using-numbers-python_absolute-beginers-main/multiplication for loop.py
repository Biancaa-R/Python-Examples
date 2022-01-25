
y= int(input("enter the number to find multiplication table"))
z=int(input("enter the number of rows"))

for i in range(0,z+1):

    if i==0:
        continue
    if y==0:
        print("error")
        break

    print(i ,"x", y,"=",i*y)

    sum_=0
    sum_=sum_+i*y 
    
    print( "the sum of the multiplied terms till now is",sum_)
   

print("the cummulaive frequency is")
for i in range(0,z+1):

    if i==0:
        continue
    if y==0:
        print("error")
        print("the number to be multiplied cannot be zero")
        break

    sum_=0
    sum_=sum_+i*y

    print(sum_)
