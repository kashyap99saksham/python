# USE OF FUNCTION IN PYTHON
def add_two(a,b):
    return a,b
print(add_two("SAKSHAM",87))

# PROBLEM : PASS NAME TO FUNCTION ,RETURN LAST LETTER OF NAME
def last_letter(name):
    return(name[len(name)-1])
name = input("enter your name")
print(last_letter(name))

def odd_even(a):
    return a%2 == 0     #GOOD WAY TO PROGRAM , OUTPUT : TRUE||FALSE
print(odd_even(10))

# PROBLEM : GREATEST NO. OF TWO
def greatest(a,b):
    if a>b:
        return a
    return b 
print(greatest(4,7))   

# PROBLEM : GREATEST NO. OF THREE
def greatest2(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
print(greatest2(3,6,2))

# PROBLEM : PALINDROME - NAMAN
def is_palindrome(n):
    return n == n[::-1]
print(is_palindrome("naman"))
print(is_palindrome("saksham"))
    

# PROBLEM : FIBONACCI SERIES - 0 1 1 2 3 5 8 13 21 34.....
def fibbo(n):
    a=t=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
        t = a+b
        a = b
        b = t
        print(t,end = " ") 
fibbo(8)
   
# IMPORTANT RULE ABOUT FUNCTION PARAMETERS
# def fun(name="Unknown",age,phone)   ERROR : CANT MAKE DEFAULT PARAMETER AS FIRST PARAMETER, ALWAYS MAKE IT AS LAST
# def fun(name,age,phone = None)      --CORRECT
# def fun(name = "unknown" ,age = None,phone=None)    --CORRECT      

# HOW TO CHANGE GLOBAL VARIABLE VALUE IN ANY FUNCTION
x = 5
def change_x():
    global x 
    x = 7
    return x
print(change_x())

