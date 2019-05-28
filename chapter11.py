#CHAPTER : FUNCTION
# USE OF *OPERATOR : WE CAN GIVE MULTI VALUE WITH TAKING TOO MANY ARGUMENTS
def sum(*args):
    t = 0
    for i in args:
        t += i
    return t
print(sum(1,2,3,4,5,6,6,7))

def sum(s,*args):       #THIS 1 IS ALLOCATED TO S
    t = 0
    for i in args:
        t += i
    return t
print(sum(1,2)) 

def sum(*args):       #THIS 1 IS ALLOCATED TO S
    t = 0
    for i in args:
        t += i
    return t
p = [1,2,3]
#print(sum(p))       #GIVES ERROR BECAUSE LIST IS PASSING SO USE *P
print(sum(*p))  #UNPACK ANY DATA STRUCTURE OUTPUT : 6


# PROBLEM : GIVE TWO ARGUMENT , FIRST -ANY NUMBER | SECOND - (TUPLE OR LIST) ---> OUTPUT IS LIST ITEMS ** FIRST NUMBER
def expo(n,*args):
    ex = []
    for i in args:
        ex.append(i**n)
    return ex
li = [1,2,3,4]
print(expo(2,*li)) #output:[1, 4, 9, 16]

# USING LIST COMPRHENSION
li = [1,2,3,4]
n=2
print([i**n for i in li])     #output:[1, 4, 9, 16]

# USE OF KWARGS(**) : THIS IS OPTIONAL MEANS USER CAN LEAVE OR GIVE THE VALUE OF KWARGS
def fun(**kwargs):      #TAKE VALUES AS DICTIONARY
    print(kwargs)       #{'name': 'saksham', 'age': 20}
fun(name = 'saksham' , age = 20)

# OR
def fun(**kwargs):      #TAKE VALUES AS DICTIONARY
    print(kwargs)       #{'name': 'saksham', 'age': 20}
d = {'name':'saksham' , 'age':20}
fun(**d)          #DICTIONARY UNPACKING)

# MAKE PRGM GIVE REVERSE LIST NAME WITH FIRST LETTER CAPITAL IF USER SAID ELSE MAKE FIRST LETTER CAPITAL
def rev(l, **kwargs):
    if kwargs.get('rev') == True:
        return [i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]
l = ['saksham','kashyap']
print(rev(l))       #['Saksham', 'Kashyap']
print(rev(l,rev = True))    #['Mahskas', 'Payhsak']


