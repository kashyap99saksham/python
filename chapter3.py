# USE OF 'IF' || 'ELSE' LOOP
age = int(input("Enter Your Age"))
if age>=18:
    print("You are eligible")
else:
    print("OOPS! you are not eligible")
#USE OF PASS STATMENT   : ALLOWS TO PASS BLOCK
if age>=18:
    pass    

#EXERCISE
# PROBLEM  :  GUESSING GAME
n = 437
g = int(input("Enter any no."))
if g==n:
    print("HURRRAH!! YOU WIN")
else:
    if g>n:
        print("OOPS! TOO HIGH")
    else:
        print("OOPS! TOO LOW")


#AND , OR CONDITION
name = "sakti"
age = 20
if name=="sakti" and age==20:
    print("TRue")

#PROBLEM
name,age = input("Enter Your Name and age ").split()
age = int(age)
if age >= 18 and (name[0]=="A" or name[0]=="a"):
    print("TRUE")
else:
    print("FALSE")
    

# IF WITH 'IN'
name = "saksham"
if 'a' in name:
    print("a is present in name")
else:
    print("OOPS!")


# CHECK EMPTY OR NOT
name = ""
if name:
    print("name is not empty") 
else:
    print("name is empty")


# USE OF LOOPS
# WHILE LOOP || FOR LOOP
i = 1
while i<=10:
    print(f"HELLO SAKSHAM {i}")  #Print it 10 times
    i += 1

# SUM : 1 TO 20 NO. [USING WHILE LOOP]
i = sum = 0
while i<=10:
    sum += i
    i += 1
    print(f"sum is {sum}")

# PROBLEM : PRINT SUM OF N NATURAL NO.
n = int(input("Enter any no."))
i = 1
sum = 0
while i<=n:
    sum += i
    i += 1
    print(f"sum is {sum}")

# PROBLEM : PRINT THE SUM OF DIGITS
n = input("Enter any number more than one digit")
i=sum=0
while i<len(n):
    sum += int(n[i]) 
    i += 1
print(sum)        

# PROBLEM : COUNT ALL CHARACTER IN NAME
name = input("Enter Your Name ")
i = 0
temp = ""
while i<len(name):
    if name[i] not in temp:
        temp += name[i]    
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1


# USE OF INFINITE LOOP
while True:
    print("Hello WOrld")

# USE OF FOR LOOP WITH RANGE FUNCTION
for i in range(10):     # i=0 to 9
    print(f"Hello : {i}")
for i in range(1,11):    #i=1 to 10
    print(f"Hello : {i}")

# EXAMPLE : SUM OF N NO.
n = int(input("Enter any no."))
total = 0
for i in range(1,n+1):
    total += i
print(f"sum is {total}") 

# EXAMPLE : SUM OF EVERY DIGITS
n = input("Enter any no.")
val = 0
for i in range(0,len(n)):
    val += int(n[i])
print(f"SUM IS : {val}")

# EXAMPLE : COUNT ALL CHARACTER IN USER'S NAME
name = input("Enter your name")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        temp += name[i] 
        print(f"{name[i]} : {name.count(name[i])}")

# USE OF BREAK AND CONTINUE KEYWORD
for i in range(1,11):
    if i == 9:
        break       #HALT WHOLE LOOP
    if i == 5:
        continue    #JUMP EXECUTION TO FOR LOOP IGNORE BELOW CODE
    print(i)


# MODIFY GUESSING GAME
import random       #IMPORT RANDOM MODULE
num = random.randint(1,100)     #GENERATES RANDOM NUMBER
count = 0
for i in range(1,21):
    g = int(input("GUESS any no. between 1 to 100 "))
    count += 1 
    if g==num:
        print(f"HURRRAH!! YOU WIN YOUR TOATAL GUESS NO. {count} ")
        break
    else:
        if g>num:
            print("OOPS! TOO HIGH")
        else:
            print("OOPS! TOO LOW")

# SHORTCUT TO PRINT EVEN AND ODD NO.
for i in range(0,101,2):      #2 is step arguement
    print(i)

# UNIQUE THING IN PYTHON
n = input("Enter any digit.")
total = 0
for i in n:     # all value are iterate in i
    val = int(i)
    total += val   
print(total)
        OR
name  = "saksham"
for i in name:
    print(i)    Output = saksham

