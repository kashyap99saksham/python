print('Hello World') 
#both is correct way
print("saksham")
print("I 'am' saksham")     #right
print('I "am" saksham')     #right
#print("I "am" saksham")     #error
#print('I 'am' saksham')     #error
print('I \'am\' saksham')      #USE BACKSLASH BEFORE COLON, TO USE SAME COLON IN A LINE(REMOVE PREVIOUS ERROR)
print("I \"am\" saksham")      #NEVER USE SAME COLON WITHOUT BACKSLACH
print("This is double backslash \\\\")     #NEVER USE SINGLE BACKSLASH! - DOUBLE BS. = SINGLE BS.
print("This is single \\ backslash")        #ALWAYS USE DOUBLE BS. WHEN SINGLE NEEDED
print("This is z\b backspace")      #DELETE PREVIOUS LETTER
#print("This is comment")
print("Line A\n Line b")    #NEW LINE
print("My Name is \t saksham")  #TAB SPACE

#OUTPUT : Line A \n Line b
print("Line A \\n Line b")
#OUTPUT : \" \'
print(" \\\" \\\' ")    #\\ is for \ and \" is for "

#EXCERCISE - 1
#OUTPUT : This is \\double backslash
#OUTPUT : This is /\/\/\/\/\/\mountain
#OUTPUT : He is     awsome
#OUTPUT : \" \n \t \'
#SOLUTION
print("This is \\\\double backslash")
print("This is /\\/\\/\\/\\/\\moutain")
print("He is \t awsome")
print(" \\\" \\n \\t \\\' ")

#----------KHATARNAAK SHORTCUT-----------
print(r"This is \\double backslash")
print(r"This is /\/\/\/\/\moutain")
print(r" \" \n \t \' ")

#PRINT EMOJI'S 
print("\U0001F923")     #COPY U+1F923 FROM https://unicode.org/emoji/charts/full-emoji-list.html . WRITE \ IN FRONT AND REPLACE + WITH 000          
print("\U0001F618")

#PRINT AS CALC
print(2+5)
print(2+5*2)
print(3%2)  #MODULO- GIVES REMINDER
print(4/2)  #FLOATING POINT DIVISION (RECOMMENDED)
print(4//2) #INTEGER DIVISION
print(2**3)    #EXPONENTIAL(2POWER3)
print(2**0.5)   #UNDER ROOT 2
print(round(2**0.5,4))    #ROUND OFF UPTO 4 DIGITS AFTER POINT

# #PRECEDENCE AND ASSOCIATIVITY RULE
# HIGHEST PRECEDENCE  -   ASSOCIATIVITY 
# ()                 
# EXPONENT            :   RIGHT TO LEFT     PRINT(2**3**4) : 3**4 = 81 || print(2**81) = 2417851639229258349412352
# *,/,//,%            :   LEFT TO RIGHT
# +,-                 :   LEFT TO RIGHT

#NEVER USE SPECIAL SYMBOLS IN VARIABLE NAME, EXCEPT _ AND NUMERIC
 
_name = "saksham"
user_name = 'saksham'
s1name = "saksham" 
