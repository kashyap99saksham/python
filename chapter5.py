# INTRODUCTION TO DATA STRUCTURE
# LIST : CAN STORE ANYTHING IN LIST - INT,FLOAT,STRINGS
# add and delete : append,insert,extend || pop,del,remove 
num = [1,2,3,4,5]
word = ['one',"two","three"]
mixed = [1,2,3,4,"five","six",7.0]
print(f"{num} \n{word}\n{mixed}")

# SLICING WITH LIST : SIMLILAR TO STRING SLICING
print(word[::-1])
mixed[1] = "two"        #LIST ARE MUTABLE BUT STRINGS ARE IMMUTABLE
print(mixed)
mixed[2:] = "three"     #OUTPUT : [1, 'two', 't', 'h', 'r', 'e', 'e']
print(mixed)

# HOW TO ADD ITEMS IN LIST
# USE APPEND METHOD
fruits = ["apple","grapes"]
fruits.append("mango")      #ADD ITEM AT END
print(fruits)

color = []
color.append("black","red") #ERROR | APPEND() ADD ONLY ONE ARGUEMENT AT A TIME
color.append("black")       #ADD ITEMS IN BLANK LIST
print(color)

# USE INSERT METHOD
color = ["red","green"]
color.insert(1,"blue")      #1 - POSITION OF INSERTION || OUTPUT:['red', 'blue', 'green']
print(color)

#USE OF EXTEND METHOD : IT CONCATINATE LISTS
fname = ["saksham"]
lname = ["kashyap"]
fname.extend(lname)
print(fname)

# DELETE ITEMS FROM LIST : POP METHOD - DELETE LAST ITEM FROM LIST
color = ["red","blue","black","violet","green"] 
color.pop()     #DELETE LAST ITEM | output : ["red","blue","black","violet"]
print(color)
color.pop(2)    #output: ['red', 'blue', 'violet']
print(color)

# POP METHOD RETURN POPPED VALUE SO THAT YOU CAN SAVE
s = [2,4,6,]
popped_val = s.pop()
print(popped_val)       #output :6

# USE OF DELETE OPERATOR
color = ['red', 'blue', 'violet']
del color[2]
print(color)    #output : ['red', 'blue']

# USE OF REMOVE METHOD : WHEN WE DONT KNOW LOCATION - REMOVE ITEM BY ITS NAME
color = ['red', 'blue', 'violet']
color.remove("violet")
print(color)

color = ['red', 'blue', 'red','violet']
color.remove("red")     #REMOVE FIRST RED FROM LIST | OUTPUT :['blue','red', 'violet']

# USE OF IN in LIST
color = ['red', 'blue', 'violet']
if "red" in color:
    print("PRESENT")

# USE OF COUNT IN LIST : SAME AS IN STRING
color = ['red', 'blue', 'violet']
print(color.count('red'))
# color.len()     ERROR:length is not member of list

# USE OF SORT METHOD IN LIST
color = ['red', 'blue', 'violet']
color.sort()        #sort list in ascending order 
print(color)
num = [1,7,3,6,2,5,4]
num.sort()
print(num)
# USE OF SORTED FUNCTION
print(sorted(num))

# USE OF CLEAR METHOD
num = ['red', 'blue', 'violet']
num.clear()     #MAKE LIST EMPTY | OUTPUT : []
print(num)

# USE OF COPY METHOD : COPY THE LIST
num = [1,2,1,3]
num_copy = num.copy()
print(num_copy)

# CONVERTING STRING INTO LIST
name = "saksham kashyap".split()        #output : ['saksham', 'kashyap']
print(name)
fname,lname = "saksham,kashyap".split(",")
print(fname)
print(lname)

# USE OF JOIN METHOD IN LIST : CONVERT LIST INTO STRING
name = ["saksham",'kashyap']
print(" ".join(name))       #convert list into string | output :saksham kashyap

# FOR LOOP WITH LIST
fruits = ['apple','grapes','banana','kiwi']
for fruit in fruits:
    print(fruit)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    for j in i:
        print(j)

# USE OF TYPE()
s = "saksham"
print(type(s))      #output:string

# GENERATE LIST WITH RANGE FUNCTION
print(list(range(1,11)))

# USE OF INDEX METHOD : TELLS INDEX OF ITEM IN LIST
lst = list(range(1,11))
print(lst.index(4))     #output : 3

lst2 = [1,2,3,4,5,6,1,8,9]
print(lst2.index(1,2))     #2-starting point | 1-searching item

# PROBLEM : PASS LIST TO FUNCTION AND RETURN NEGATIVE LIST
def negative_list(f):
    nega = []
    for i in f:
        nega.append(-i)
    return nega
lis = list(range(1,11))
print(negative_list(lis))

# PROBLEM : RETURN square_of_list
def square_of_list(l):
    sl = []
    for i in l:
        sl.append(i*i)
    return sl
lis = list(range(1,11))
print(square_of_list(lis))


# WE CAN REVERSE OUR LIST DIRECTLY BY USING DIRECT SLICING [::-1] AND USING 
# list.reverse()

# PROBLEM : RETURN REVERSE OF LIST WITHOUT USING DIRECT SLICING [::-1]
def reverse(l):
    rev = [] 
    for i in range(len(l)):
        rev.append(l.pop())
    return rev
lis = list(range(1,11))
print(reverse(lis))

# PROBLEM : RETURN LIST WITH REVERSE OF EVERY ELEMENT IN THAT LIST
def reverse_every(l):
    rev2 = []
    for i in l:
        rev2.append(i[::-1])
    return rev2
lis = ["saksham",'aditi','kashyap']
print(reverse_every(lis))


# PROBLEM : FILTER ODD AND EVEN LIST
def odd_even(l):
    even = []
    odd = []
    for i in range(0,len(l),2):
        even.append(i)
    for j in range(1,len(l),2):
        odd.append(j)
    oe = [even,odd]
    return oe
lis = list(range(0,10))
print(odd_even(lis))


# PROBLEM : RETURN COMMON ELEMENTS IN TWO LISTS
def common(l1,l2):
    c = []
    for i in l1:
        if i in l2:
            c.append(i) 
    return c
l1 = [1,2,5,8]
l2 = [1,2,7,5,6]
print(common(l1,l2))
         
# USE OF MAX() AND MIN() FUNCTION
l1 = [1,2,5,8] 
print(min(l1))      #op : 1
print(max(l1))      #op : 8

# PROBLEM : RETURN NO. OF LISTS IN MAIN LIST
def count_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1 
    return count
l = ['a',[1,2],[3,4],'b',['c']]
print(count_list(l))

# ADD TWO LIST
a = [1,2,3,4]
b = [5,6,7,8]
print(a+b)