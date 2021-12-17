def call(p=40,q=20):
    global x
    p+= q
    q-= p
    x+= q
    print(x,"#",q)
x,q,r=10,20,30
r=call()
print(x,q,r)
q=call(x)
print(x,q,r)
