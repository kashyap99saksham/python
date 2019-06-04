# #PASS FUNCTION AS AN ARGUEMENT 
# # HOW TO MAKE MAP FUNCTION BY  YOURSELF
# # WHAT MAP FUNCTION DO : MAP(FUNCTION,L) - WE CALL MAP FUNCTION AND PASS TWO ARGU., ONE IS FUNCTION AND SECOND IS LIST 
# # HOW MAP FUNCTION DO WORK PRACTICALLY
# def square(a):
#     return a**2
# l = [1,2,3,4,5]
# print(list(map(square,l)))      #[1, 4, 9, 16, 25]

# # NOW SEE THE INTERNAL WORKING OF MAP()
# # LETS CREATE MAP BY YOURSELF
# def my_map(func,l):
#     lis = []
#     for i in l:
#         lis.append(func(i))
#     return lis
# print(list(my_map(square,l)))      #[1, 4, 9, 16, 25]


# # WE CAN USE LAMBA FUNCTION ALSO AS AN ARGUEMENT
# print(my_map(lambda b : b**2 , l))  #[1, 4, 9, 16, 25]

# # USE OF FUNCTION return FUNCTION - KNOWN AS CLOSURE
# def outer_func():
#     def inner_func():
#         print("Hello saksham")
#     return inner_func
# fun = outer_func()
# fun()       #Hello saksham

# # PRACTICAL USE OF RETURNING FUNCTION
# # MAKE A PROGRAM OF RETURNING THE EXPONENTIAL VALUES
# def power(x):
#     def calc(val):
#         return val**x
#     return calc
# square = power(2)
# print(square(4))

# cube = power(3)
# print(cube(4))

# # INTRODUCTION OF DECORATORS :- IT INCREASES THE FUNCTIONALITY OF OTHER FUNCTIONS
# # SUPPOSE WE WANT TO PRINT ADITIONAL LINES BEFORE ANY FUNCTION WITHOUT CHANGING IN FUNCTION
# # SO WE HAVE TO USE DECORATORS
# def decorators_func(fun):
#     def wrapper_func():
#         print("I M DECORATOR")
#         fun()
#     return wrapper_func
# def func1():
#     print("I m function 1")
# wf = decorators_func(func1)
# wf()    #I M DECORATOR    I m function 1

# # USE OF @ : USE OF DECORATOR
# def decorators_func(fun):
#     def wrapper_func():
#         print("I M DECORATOR")
#         fun()
#     return wrapper_func

# @decorators_func      #SHORTCUT
# def func1():
#     print("I m function 1")
# func1()     ##I M DECORATOR    I m function 1

# # MAKE A PROPER DECORATOR WHICH CAN TAKE VALUES AS WELL
# def decorators_func(fun):
#     def wrapper_func(*args,**kwargs):
#         print("I AM DECORATOR")
#         fun(*args,**kwargs)
#     return wrapper_func

# def func1(a):
#     print(f"I m func1 with value of {a}")

# func1 = decorators_func(func1)
# func1(5)        #I AM DECORATOR      I m func1 with value of 5


# # NOW MAKE FUNCTION RETURNING VALUES
# def decorators_func(fun):
#     def wrapper_func(*args,**kwargs):
#         print("I AM DECORATOR")
#         #fun(*args,**kwargs)     #IT DOES NOT RETURN VALUE WHICH IS CALCULATED IN FUNCTION
#         return fun(*args,**kwargs)
#     return wrapper_func

# def func1(a,b):
#     return a+b

# func1 = decorators_func(func1)
# print(func1(5,3))        #8


# #USE OF DOC STRING
# def doc_string():
#     """THIS IS DOC STRING """
#     pass

# print(doc_string.__doc__)       #THIS IS DOC STRING
# print(doc_string.__name__)      #doc_string

# def decorators_func(fun):
#     def wrapper_func(*args,**kwargs):
#         """I AM DOCSTR OF WRAPPER_FUNCTION"""
#         return fun(*args,**kwargs)
#     return wrapper_func

# @decorators_func  #it call decorator_func(func1) and store func1 = wrapper_func
# def func1(a,b):
#     """I AM DOCSTR OF FUNC1 FUNCTION"""
#     return a+b
# print(func1.__doc__)        #I AM DOCSTR OF WRAPPER_FUNCTION        coz func1 = wrapper_func


## PROBLEM : OUTPUT -
## You are calling add function 
## This function takes two no as parameter and return their sum
## 9  

# def decorator_func(fun):
#     def wrapper_func(*args,**kwargs):
#         print(f"You are calling {fun.__name__} function")
#         print(fun.__doc__)
#         return fun(*args,**kwargs)
#     return wrapper_func

# @decorator_func
# def add(a,b):
#     """This function takes two no as parameter and return their sum"""
#     return a+b
# print(add(5,4))     #You are calling add function       This function takes two no as parameter and return their sum    9


# # CALCULATE TIME OF FUNCTION
# import time
# def calculate_time(function):
#     def wrapper_func():
#         t1 = time.time()
#         function()
#         t2 = time.time()
#         t = t2-t1
#         print(f"TIME TAKEN BY {function.__name__} is {t}")
#     return wrapper_func

# @calculate_time
# def fun1():
#     print("HELLO")
#     print("HELLO")
#     print("HELLO")

# fun1()      #HELLO  HELLO   HELLO   TIME TAKEN BY fun1 is 0.0020661354064941406


# ONLY INT CAN PASS IN FUNCTION
# SIMPLE WAY 
# def summ(*args):
#     tot = 0
#     for i in args:
#         tot += i
#     return tot
# print(summ(1,2,3,4,5,*[1,2,3,4,5]))

# # USING DECORATOR SOLVE THIS PROBLEM
# def summ_decorator(fuction):
#     def wrapper_func(*args):
#         a=[]
#         for i in args:
#             a.append(type(i)==int)
#         if all(a):
#             return func1(*args)
#     return wrapper_func 
    
# @summ_decorator
# def func1(*args):
#     t=0
#     for j in args:
#         t+=j
#     return t

# print(func1(5,4))

