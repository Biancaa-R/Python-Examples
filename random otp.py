#Program to generate a 6 digit random otp
#method 1
import random
y=random.randrange(100000,999999)
print("Your otp is:",y)

#method 2
import random
x=random.randint(100000,999999)
print("Your otp is:",x)

#Generating random text from the random number
def txtotp(y):
    otp=""
    a=0
    values=["A","B","C","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    y=str(y)
    y=list(y)
    for i in y:
        i=int(i)
        a+=i
        if a<=51:
            otp+=values[a]
        else:
            a=0
            a+=i
            otp+=value[a]
    print("Your text otp is",otp)        
txtotp(y)
txtotp(x)
            
