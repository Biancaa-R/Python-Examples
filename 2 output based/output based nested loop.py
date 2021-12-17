#Code snippet 1
#Nested loops
for i in range(3):
	for j in range(3):
		print(i,j)

"""output:
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2 """

#code snippet 2:
for i in range(3):
	for j in range(3):
	    for k in range(3):
		    print(i,j,k)

'''		   
0 0 0
0 0 1
0 0 2
0 1 0
0 1 1
0 1 2
0 2 0
0 2 1
0 2 2
1 0 0
1 0 1
1 0 2
1 1 0
1 1 1
1 1 2
1 2 0
1 2 1
1 2 2
2 0 0
2 0 1
2 0 2
2 1 0
2 1 1
2 1 2
2 2 0
2 2 1
2 2 2'''

#Code snippet3:
for i in range(5):
	for j in range(i):
	    for k in range(j):
		    print(i,"#",j,"#",k)

#output
"""		    
2 # 1 # 0
3 # 1 # 0
3 # 2 # 0
3 # 2 # 1
4 # 1 # 0
4 # 2 # 0
4 # 2 # 1
4 # 3 # 0
4 # 3 # 1
4 # 3 # 2"""