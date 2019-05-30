# ENUMERATE FUNCTION : for counter,name in enumerate(l) : IT START COUNTER AUTOMATICALLY 
# PROBLEM: FIND LOCATION OF STRING IN A LIST
def fun(l,target):
    # counter = 0
    if target in l:
        for counter,name in enumerate(l):
            if name == target:
                return counter
    else:
        return -1                        


l = ['s','a','k','s','h','a','m']
# f = 'sham'
print(fun(l,'p'))

# USE OF FILTER FUNCTION : CAN BE ITERATE ONLY ONCE
def even(*l):
    for i in l:
        return i%2==0
n = [1,2,4,5]
f = list(filter(even,n))    #IT FILTER TRUE VALUES
print(f)


# USE OF ZIP() FUNCTION : IT ZIP BOTH VALUES TOGETHER
li1 = ['name','age','height']
li2 = ['saksham',20,6]
print(list(zip(li1,li2))) #WE CAN CONVERT THIS OBJECT INTO ANY DATA STRUCTURE LIKE DICT ETC        #[('name', 'saksham'), ('age', 20), ('height', 6)]
#IF li2 HAVE MORE VALUES THEN IT ZIP THAT MUCH VALUES WHICH ARE IN li1


# WE CAN UNPACK USING ZIP ALSO
l = [(1,4),(2,6),(6,9),(5,3)]   #WE CAN UNPACK THIS INTO DIFF. LISTS
l1,l2 = zip(*l)
print(list(l1))         #[1, 2, 6, 5]
print(list(l2))         #[4, 6, 9, 3]


# HARD-PROBLEM : FIND AVERAGE OF FIRST VALUE OF ANY NO. OF LIST USE LAMBA  
SIMPLE WAY
def average_finder(*args):
        av = []
        for i in zip(*args):
                av.append(sum(i)/len(i))
        print(av)
 NOW PRGM IN SINGLE LINE
average_finder = lambda *args:[sum(i)/len(i) for i in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))


# USE OF ANY AND ALL FUNCTION
# MAKE PROGRAM TO CHECK ALL NO. IN LIST ARE EVEN OR NOT
# FIRST MAKE IT BY SIMPLE WAY
l = [2,3,5,6,7]
t = [True if i%2==0 else False for i in l]
# NOW USE OF ALL FUNCTION ---> IF ALL VALUES IN LIST IS TRUE IT PRINTS TRUE ANF IF ANY VALUE IS FALSE IT GIVES FALSE
# all([True,True,True])------> True
# all([True,True,False])------> False
print(all(t))   #output : False

# NOW USE OF ALL FUNCTION ---> IF ANY VALUES IN LIST IS TRUE IT PRINTS TRUE ANF IF ALL VALUE IS FALSE IT GIVES FALSE
print(any(t))           #output : True


