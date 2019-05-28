# INTRO OF LAMBDA EXPRESSIONS(ANONYMUS FUNCTION)
add = lambda a,b : a+b      #USE ADD AS A NORMAL FUNCTION
print(add(2,3))     

# MAKE IS_EVEN ODD PRGM USING LAMBA FUNCTION
e_o = lambda a : a%2==0
print(e_o(4))

# OR USING IF ELSE
e_o = lambda a : True if a%2==0 else False
print(e_o(4))



# PRINT LAST CHAR OF STRING USING LF
lc = lambda s : s[-1]
print(lc('saksham'))