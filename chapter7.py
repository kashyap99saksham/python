# INTRODUCTION TO DICTIONARY : UNORDERED COLLECTION OF DATA | ITEMS ARE NOT LOCATED IN ORDER
# DICTIONARY HAVE KEY VALUE PAIR

student = {'name':'saksham', 'age':20}
print(student)          #{'name': 'saksham', 'age': 20}

# SECOND WAY TO CREATE DICTIONARY
user = dict(name = 'saksham',age = 20)
print(user)             #{'name': 'saksham', 'age': 20}

#ACCESSING ITEM IN DICTIONARY 
student = {'name':'saksham', 'age':20}
#print(student[0])           #ERROR | ITEMS ARE NOT LOCATED IN ORDER
print(student['name'])      #OUTPUT : SAKSHAM
stu = dict(name = 'saksham')
print(stu['name'])      #OUTPUT : SAKSHAM

# STORE ANYTHING IN DICT : string,number,list,dict
user = dict(
    name = 'saksham',age = 20,
    lis = ['sak','sham'],
    dic = {'name':'saksham'}
    )
print(user['dic'])      #output: {'name':'saksham'}

users = dict(
    user1 = dict(name = 's',age = 19),
    user2 = dict(name = 'a',age = 20)
)
print(users['user1'])

# # HOW TO ADD ITEM TO EMPTY DICT
di = {}
di['name'] = "saksham"
di['age'] = 20
di['dob'] = 2501199
print(di['name'])       #OUTPUT : SAKSHAM
print(di['age'])       #OUTPUT : 20
print(di['dob'])       #OUTPUT : 2501199

# USE OF IF WITH in IN DICT : CHECK KEY IN DICT OR NOT
di = dict(name = 'saksham')
if 'name' in di:
    print("present")
else:
    print('not present')

# CHECK VALUES PRESENT OR NOT
d = dict(n = 1,nn = 'saksham')
if 1 in d.values():
    print("present")
if 'saksham' in d.values():
    print("present")


d = dict(n = 1,nn = 'saksham')
for i in d:     #i contain all key 
    print(i)        #OUTPUT: n  nn
OR
d = dict(n = 1,nn = 'saksham')
for i in d.keys():     #i contain all key values
    print(i)        #OUTPUT: n  nn


d = dict(n = 1,nn = 'saksham')
for i in d.values():     #i contain all values
    print(i)        #OUTPUT: n  nn

#USE OF ITEM() : VERY USEFULl
d = dict(n = 1,nn = 'saksham')
print(d.items())        #Op : dict_items([('n', 1), ('nn', 'saksham')])

# ITEM() : VERY USEFULl
d = dict(n = 1,nn = 'saksham')
for i,j in d.items():       #i = keys and j = items
    print(f"key is {i} aNd Items are {j} ")     #key is n aNd Items are 1 || key is nn aNd Items are saksham

# HOW TO ADD AND DELETE DATA IN DICT
# ADD
d = dict(n = 1,nn = 'saksham')
d['nnn'] = 'kashyap'
print(d)        #{'n': 1, 'nn': 'saksham', 'nnn': 'kashyap'}

#POP: DELETE THE KEY AND RETURN THE VALUES OF THAT KEY
popped_value = d.pop('nnn')
print(popped_value)     #OP: kashyap

#POPITEM METHOD : USED TO DELETE RANDOM key with values 
popped_data = d.popitem()
print(popped_data)  #OP :('nn', 'saksham')
print(type(popped_data))        #tuple

# USE OF UPDATE() HOW TO ADD DATA IN DICT
d = dict(n = 1,nn = 'saksham')
d1 = dict(fn = 'sak',ln = 'sham')
d.update(d1) 
print(d)        #{'n': 1, 'nn': 'saksham', 'fn': 'sak', 'ln': 'sham'} 

# USE OF FROMKEY() FUNCTION : USED TO MAKE KEYS DEFAULT VALUES 
d = dict.fromkeys(['name','age'],'unknown')
print(d)        #{'name': 'unknown', 'age': 'unknown'}
c = dict.fromkeys(range(1,6),'none')        
print(c)        #{1: 'none', 2: 'none', 3: 'none', 4: 'none', 5: 'none'}

# GET() METHOD (USEFULL) : GIVE VALUES OF KEYS AND SPECIAL THING IS - IF VALUE IS NOT PRESENT IN KEY IT GIVE 'NONE' NOT ERROR
d = dict.fromkeys(range(1,3),"saksham")
print(d.get(2))  #op : saksham || get value of 2 key = saksham
# BUT
print(d.get(10))    #op : none || SPECIALITY
print(d)

if d.get(2):        #EASY WAY TO CHECK
    print("present")   #OP : present

# USE OF CLEAR() METHOD
d.clear()
print(d)    #op : {}
 
d = dict.fromkeys(range(1,3),"saksham")
c = d.copy()    #COPY DATA OF D TO C
print(c)

#SOMEPEOPLE THINK C = D --> BUT THIS NOT MAKE COPY , THERE IS ONLY ONE DICT. , CAN BE ACCES BY BOTH
# EXPLAIN THROUGH EXAMPLE
d = dict.fromkeys(range(1,3),"saksham")
c = d
c.pop(2)
print(d)    #HERE WE ARE PRINTING D BUT WE POP FROM C. IT MEANS BOTH ARE SAME . C IS NOT A NEW COPY    

# MORE ABOUT GET()
d = dict.fromkeys(range(1,3),"saksham")
print(d.get(10,"KEY NOT FOUND!!"))      #OP : KEY NOT FOUND


# KEYS WITH SAME NAME CANT POSIBLE 
d = dict(name = "saksham",age = 19,age = '20')
print(d)  #ERROR

# PROBLEM : RETURN DICT., CUBE FINDER UPTO Nth NUMBER
# OUTPUT - {1:1,2:8,3:27}
def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube
print(cube_finder(5))


# PROBLEM : RETURN DICT OF WORD COUNTER || THERE IS NO NEED TO CHECK SAME WORDS 
def word_counter(name):
    w_c = {}
    for i in name:
        w_c[i] = name.count(i)
    return w_c
print(word_counter('saksham'))
        

# PROBLEM: TAKE INPUT FROM USER AND PRINT NAME , AGE , FAV_MOVIE ,FAV_SONG IN DIFFRENT LINES

n = input("Enter your name ")
a = input("Enter Your Age ")
f_m = input("Enter Your fav_movies(comma seperated) ").split(",")
f_s = input("Enter Your fav_songs(comma seperated) ").split(",")
dic = {}
dic['name'] = n
dic['age'] = a
dic['fav_movies'] = f_m
dic['fav_songs'] = f_s
for i,j in dic.items():         #VERY VERY IMPORTANT CONCEPT
    print(f"{i} : {j}")    