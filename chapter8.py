# INTRODUCTION TO SETS
# UNORDERED COLLECTION OF UNIQUE DATA :- NO INDEXING
s = {1,4,2,6,'saksham'}
# print(s[1]) ERROR  
# SAME DATA IS IS CONVERTED INTO SINGLE DATA : S = {2,3,5,2} | OUTPUT : 2,3,5

# USE OF SET : REMOVE DUPLICATE DATA
l = [1,4,6,2,7,2,1,2,1,6,5]
s = list(set(l))
print(s)

# ADD DATA INTO SETS
s = {1,4,2,6}
s.add(5)
s.add(8)
s.add(7)
print(s)

#REMOVE DATA FROM SETS
s = {1,4,2,6,8,9}
s.remove(4)
print(s)
# USE OF DISCARD METHOD: IT DOES NOT GIVE ERROR IF REMOVABLE ITEM IS NOT PRESENT IN SET
s.discard(4) #does not give anything without error
# USE OF CLEAR METHOD : CLEAR ALL SET
s.clear() 
print(s)
# USE OF COPY METHOD
s1 = s.copy()
print(s1)

# IMORTANT THING ABOUT SET : WE CANT STORE LIST AND DICTIONARY IN SET
s = {1,4,2,6,8,9,[2,4,6,3,2],{'n':43,'a':3}}    #ERROR | LIST AND DICT ARE STORED IN SETS


#NEW IN SET : OPERTAIONS - UNION , INTERSECTION
s1 = {1,2,3,4}
s2 = {5,4,6,1}
union_set = s1 | s2  #UNION SYMBOL |
print(union_set)    #OUTPUT : {1,2,3,4,5,6}
intersection_set = s1 & s2  #ITERSECTION SYMBOL IS &
print(intersection_set) #OUTPUT : {1,4}
