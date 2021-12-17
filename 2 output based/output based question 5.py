#Output of the python code
#code snippet 1

for name in ["Jayes","Ramya","Taruna","Suruj"]:
    print(name)
    if name[0]=="T":
        break
    else:
        print("Finished")
print("Got it")  

#code snippet 2
STR=["90","10","30","40"]
COUNT=3
SUM=0
for i in [1,2,5,4]:
    S=STR[COUNT]
    SUM=float(S)+1
    print(sum,end="")
    COUNT-=1
    
