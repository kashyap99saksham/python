# # TUPLE DATA STRUCTURE
# # TUPLE CAN STORE ANY TYPE OF VALUES
# # MOST IMPORTANT , TUPLE ARE IMMUTABLE : CANT MODIFY/CHANGES
# # NO APPEND,NO INSERT,NO POP,NO REMOVE IN TUPLE
# # TUPLE ARE FASTER THEN LIST
# t = ('a','b','c')
# print(t)

# # METHODS USED WITH TUPLES
# # COUNT : COUNT ITEM IN TUPLE
# # LEN : LENGTH OF TUPLE
# # INDEX : ITEM INDEX
# # SLICING

# # LOOPING IN TUPLE
# a = ('a','b','c')
# for i in a:
#     print(i)

# # TUPLE WITH ONE ELEMENT
# num1 = ('one')   #This is string typle ,not tuple
# num2 = ('one',)  #This is tuple
# num3 = (1)       #This is int typle ,not tuple
# num4 = (1,)      #This is tuple
# print(type(num4))   #OUTPUT : TUPLE

# # TUPLE WITHOUT PARENTHESIS
# tu = 'a','b','c','d','e'        #This is tuple
# print(type(tu))     #OUTPUT:TUPLE

# # TUPLE UNPACKING
# color = 'red','black','green','blue'
# col1,col2,col3,col4 = color     #col1=red,col2=black,col3=green,col4=blue
# print(col1)     #OUTPUT : RED

# # LIST INSIDE TUPLE
# color = 'red','black',['green','blue']
# color[2].append('white')        #OUTPUT :('red', 'black', ['green', 'blue', 'white'])
# color[2].pop()      #OUTPUT : ('red', 'black', ['green', 'blue'])
# print(color)


# # FUNCTION USED WITH TUPLE
# # MIN,MAX,SUM
# s = 1,2,3,4,5
# print(sum(s))   #OUtPUT:15

