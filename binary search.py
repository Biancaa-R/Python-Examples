#Iterative binary search function method
def binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0

    while low<=high:
        mid=(low+high)//2

        if list1[mid]<n:
            low=mid+1

        elif list1[mid]>n:
            high=mid-1

        else:
            return mid

    return -1
list1=[2,4,6,8,12,22,24,32,35,45,39,45,50,55,60]
n=int(input("Enter a number"))

result=binary_search(list1,n)

if result !=-1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in the list")
