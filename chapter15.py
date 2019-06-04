# INTRODUCTION OF GENERATORS : ARE ITERATORS
# ITERABLE = [1,2,3,4,5]
# ITERATOR = [1] THEN [2] THEN [3] THEN [4] THEN [5]

# generator function = yield ()

def fun(n):
    for i in range(1,n+1):
        yield(i)        #it makes a sequence(LESS MEMORY||FAST)
print(fun(4))
for i in fun(4):
    print(i)    #1 2 3 4
nums = fun(4)
for i in nums:
    print(i)
for i in nums:      #IT CANNOT RUN AGAIN : BECOZ IT REMOVE PREVIOUS VALUE
    print(i)

def even(n):
    for i in range(2,n+1,2):
        yield i
eve_nums = even(10)
for i in eve_nums:
    print(i)


# USE OF GENERATORS AS LIST COMPREHENSION : SIMPLE USE () IN PLACE OF []
pr = (i**2 for i in range(1,11))
for i in pr:
    print(i)

# list is taking more time then GENERATORS
# list taking more space then generator
