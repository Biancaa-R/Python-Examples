#code snippet1
p=10
q=20
p*=q//3
q+=p+q**2
print(p,q)

#code snippet2
TXT=["20","50","30","40"]
CNT=3
TOTAL=0
for C in [7,5,4,6]:
    T=TXT[CNT]
    TOTAL=float(T)+C
    print(TOTAL)
    CNT-=1

#code snippet 3
a=(2+3)**3-6/2
b=(2+3)*5//4+(4+6)/2
c=12+(3*4-6)/3
d=12%5+3+(2*6)//4
print(a,b,c,d)   

#code snippet 4
p=5/2
q=p*4
r=p+q
p+=p+q+r
q-=p+q*r
print(p,q,r)