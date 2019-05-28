# DICTIONARY COMPREHENSION        || SET COMPREHENSION
# MAKE {1:1,2:4,3:9} USING DC
print({i:i**2 for i in range(1,11)})
print({f"square of {i} is ":i**2 for i in range(1,11)})

# COUNT CHARACTERS IN STRING USING DC
name = "saksham"
print({i : name.count(i) for i in name})

# PRINT ODD EVEN VALUES IN DICTIONARY USING DC
print({i:("odd" if (i%2!=0) else"even") for i in range(1,21)})

----------------------------------------------------------------
# SET COMPREHENSION : UNORDER
print({i**2 for i in range(1,11)})

# PRINT FIRST LETTER OF NAME
name = ['saksham','kashyap','kumar']
print({i[0] for i in name})
