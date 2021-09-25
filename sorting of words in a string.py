#Enter a string separated by hyphens to get a sorted string with hyphens as the output

def sorter(val):
    val=val.lower() #upper and lower case have different values
    val=val.split("-")
    val.sort()
    val="-".join(val)
    print(val)


val=input("Enter the string")
sorter(val)
#function call
