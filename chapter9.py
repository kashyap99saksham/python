#LIST COMPREHENSION
# MAKE 1 TO 10 SQUARES 

# SIMPLE CODE
l = []
for i in range(1,11):
    l.append(i**2)
print(l)
 
# NOW , USING LIST COMPREHENSION
print([i**2 for i in range(1,11)])    #output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# WOOOW!!!!

# PRINT NEGATIVE NO. LIST FROM 1 TO 10
print([-i for i in range(1,11)])    #[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# PRINT FIRST WORD OF ALL NAMES IN LIST: NAME = ['SAKSHAM','KASHYAP','SINHA'] --> ['S','K','S']
name = ['Saksham','Kashyap','Sinha']
j = []
for i in name:
    j.append(i[0])
print(j)    #['S','K','S']
#NOW USING LC
print([i[0] for i in name])     #['S','K','S']

# REVERSE ALL NAMES IN A LIST USING LC
name = input("Enter Your Name ").split()
print([i[::-1] for i in name])  

# USE OF IF  LOOP IN LS
# MAKE ODD AND EVEN LIST
print([i for i in range(1,11) if i%2==0])
print([i for i in range(1,11) if i%2!=0])

# PRINT ONLY INT FROM LIST AND MAKE THEM STRING
def con(l):
    return [str(i) for i in l if type(i)==int]

print(con([True,False,2,43,5,None]))

# USE OF IF WITH ELSE IN LC
# MAKE ODD VALUES AS NEGATIVE AND EVEN VLUES AS MULTIPLY BY 2
print([-i if (i%2!=0)  else i*2 for i in range(1,11)])

# NESTED LIST IN LC
# PRINT : [ [1,2,3],[1,2,3],[1,2,3] ]
print([[i for i in range(1,4)] for i in range(3)])
