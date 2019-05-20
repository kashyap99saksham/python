fn = 'saksham'
ln = 'kashyap'
fn = fn + " " + ln
print(fn) 

# print("saksham" + 3)   #ERROR
print("saksham" + "3")    #NO ERROR
print("saksham" + str(3))   #NO ERROR
print(fn * 3)   #PRINT THRICE FN_VALUE

# -------------USER'S INPUT-----------
# INPUT FUNCTION ALWAYS RECIEVE VALUE IN STRING
name = input("Enter Your Name ")
print("Have a Good Day " + name)
age = input("Enter Your Age ")
print("Your age is " + age) #no error becoz input is in string

# --------------USING INT--------------
a = int(input("Enter  first no. "))
b = int(input("Enter Second no. "))
sum = a+b
print("SUM IS " + str(sum)) #WITHOUT INT, OUTPUT IS NOT SUM OF BOTH NO. OUPTUT IS IN CONCATINATION FORM


# DECLARE MUILTI VALUE IN SINGLE LINE
name , age = "SAKSHAM" , 20
print("HELLO " + name + "YOUR AGE IS " + str(age))

x = y = z = 1 #SINGLE VALUE AS MULTI VARIABLE
print(x+y+z)
 
# TWO INPUTS IN A SINGLE LINE
name , age = input("Enter your name and age seperated by space ").split()
print(name)
print(age)
name , age = input("Enter your name and age seperated by coma ").split(",")
print(name)
print(age)

#---------------- STRING FORMATTING-------------------
name ,age  = input("Enter your name and age ").split()
print("Hello " + name + " Your Age is " + str(age))     #VERY UGLY SYNTAX
print("Hello {} Your Age is {}".format(name,age))       #PYTHON 3 GOOD SYNTAX
print(f"Hello {name} Your Age is {age}")                #BEST SYNTAX IN PYTHON 3.6 [[ALWAYS REMEBER 'f' IN STARING]]


# EXERCISE
# problem : take 3 values from user and calculate total avg.
a,b,c = input("Enter Three Values (seperated by space)").split()
avg = (int(a)+int(b)+int(c))/3
print(f"AVERAGE OF VALUE IS : {avg}")


# STRING INDEXING
name = 'saksham'
# s = 0 , -7
# a = 1 , -6 
# k = 2 , -5
# s = 3 , -4
# h = 4 , -3
# a = 5 , -2
# m = 6 , -1
print(name[1])  #OUTPUT : a
print(name[-6]) #OUTPUT ; a


# STRING SLICING.
# Syntax   = [starting_index : stop_index - 1]
name = "SAKSHAM"
print(name[0:2])   #OUTPUT : SA
print(name[0:3])   #OUTPUT : SAK
print(name[1:2])   #OUTPUT : A
print(name[:])     #FULL STRING
print(name[1:])    #AFTER 1TH FULL STRING || OUTPUT : AKSHAM
print(name[:3])    #OUTPUT : SAK


# STEP ARGUEMENT
# Syntax   = [starting_index : stop_index - 1 : step]
name = "saksham"
print(name[0:7:2])         #OUTPUT : skhm
print(name[0:7:1])         #OUTPUT : saksham
print(name[::-1])          #TRICK FOR REVERSE A STRING
print(name[-1::-1])        #TRICK FOR REVERSE A STRING

# EXERCISE
# PROBLEM : TAKE USER'S NAME AND REVERSE || MAKE IT IN 2 LINES
user_name = input("Enter your name ")
print(f"Your name is {user_name[::-1]}")


# VALUES ARE PASSING THROUGH FUNCTION || METHODS ARE ALWAYS WRITTEN  WITH . (DOT) 
# USE OF LEN() FUNCTION
name = "SaKsHaM KasHyAP"
print(len(name))    #IT COUNTS THE TOTAL LENTH OF STRING WITH BLANKSPACE

# USE OF LOWER METHOD
print(name.lower())         #MAKE STRING IN LOWER CASE

# USE OF UPPER METHOD
print(name.upper())         #MAKE STRING IN UPPER CASE

# USE OF TITLE METHOD
print(name.title())         #MAKE FIRST LETTER CAPITAL AND REST ARE SMALL || OUTPUT : Saksham Kashyap

# USE OF COUNT METHOD
print(name.count("a"))         #COUNT THE LETTERS IN A STRING (case sensitive about small and capital letters)


# EXERCISE 
# PROBLEM : TAKE TWO COMMA SEPERATED INPUTS FROM USERS
# 1).USER'S NAME
# 2).A SINGLE CHARACTER
# OUTPUT : TWO LINE PRINT
# 1). USERS NAME LENGTH
# 2).HOW MANY TIMES THAT CHARACTER COMES IN NAME (CASE INSENSITIVE:COUNT ALL CASES)

# SOLUTION
name,char = input("Please Enter Your Name and single character (comma seperated) ").split(",")
name = name.lower()
print(f"YOUR NAME LENGTH : {len(name)} and {char} IS COME {name.count(char)} TIMES IN YOUR NAME")


# STRIP METHOD   :   REMOVE THE BLANKSPACES FROM STRING  
# strip()   : remove left and right blankspaces 
# lstrip()  : remove left spaces
# rstrip()  :remove right spaces
name = "    saksham    "
dots = "......."
print(name+dots)     #OUTPUT :    saksham    .......
# remove the spaces using lstrip() and rstrip()
print(name.lstrip()+dots)    #OUTPUT :saksham    .......
print(name.rstrip()+dots)    #OUTPUT :     saksham.......
print(name.strip() + dots)   #OUTPUT :saksham.......

# REPLACE METHOD : REPLACE ANY THING FROM STRING
name = "    sak      sham    "
dots = "......."
print(name.strip()+dots)    #IT CAN'T REMOVE IN BETWEEN SPACES SO USE REPLACE
print(name.replace(" " , "") + dots)    #REPLACE ALL SPACES FROM STRING
print(name.replace("sham","ti"))    
print('saksham'.replace("a","t",1))     #REPLACE ONLY FIRST a WITH t



# USE OF FIND() METHOD
print("my is name is saksham".find("is"))       #FINDS LOACTION OF CHARACTER IN STRING
c = "my is name is saksham"
is_one = "my is name is saksham".find("is")
print(c.find("is",is_one+1))        #SECOND IS LOCATION


# STRINGS ARE IMMUTABLE : STRINGS CAN NOT BE CHANGED/MODIFIED AFTER CTREATED
string = "saksham"
#string[1] = "p"     #CAN'T CHANGE/MODIFIED


