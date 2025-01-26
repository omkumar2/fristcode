#week 2

# L2.2: Variables : A Programmer's Perspective

ram_bank_balance=100000
#ram's bank balance, note that this is positive

ram_loan=500000
#ram's loan, this is to be returned by him and hence will count
#as negative

lakshman_bank_balance=2000000
lakshman_loan=10000000

net_income=ram_bank_balance+lakshman_bank_balance
#net_income is the total bank balance of the two brothers.

net_liability=ram_loan+lakshman_loan
#net_liability is the total loan of the brothers.

final_value=net_income-net_liability
#final value is the family's final money (could be +ve or -ve)
print("So, the family has", final_value)

#Variables Revisited: Dynamic Typing

#we are trying to illustrate what we call the dynamic typing
n=10
print(type(n)) #<class'int'>
print(n) #10
n=n/1
print(type(n)) #<class'float'>
print(n) #10

#More on Variables, Operators and Expressions
#next
and =4
print(and) #key word are not use as a syntax 

#next
1a=3
print(1a) #you can not used no. at stating

#next
roll=3
ROLL=112
Roll=15
print(roll,ROLL,Roll) #3 112 15       #python is case 

#next
x,y=1,2
print(x,y) #1,2       
x,y=y,x
print(x,y) #2,1

#next
x=12
print(x) #12
del x
print(x) #error

#next
count = 0
count += 1
count = count + 1
print(count)

#next
count = 5
count -= 1
count = count - 1
print(count)

#next
count = 5
count *= 2
count = count * 2
print(count)

#next
count = 5
count /= 2
count = count / 2
print(count)

#next
print("alpha" in "A variable name can only contain alpha-numeric characters and underscores") #true
print("alpha" in "A variable name must start with a letter or the underscore character") #false

#next
x = 5
print(1 < x < 10) #true
print(10 < x < 20) #false
print(x < 10 < x * 10 < 100) #true
print(10 > x <= 9) #true
print(5 == x > 4) #true

#Escape characters and types of quotes

#Escape characters 
#print('It's a beautiful day') #error
print('It\'s a beautiful day') #it's a beautiful day  , and \ this is a escape characters
print("We are from \"IIT\" Madras") #We are from IIT Madras
print('We are from "IIT" Madras') #

#next
print('My name is Om. \t\tI am from darbhanga') #My name is Om.      I am from darbhanga , \t this escape character put gape
print('My name is Om. \nI am from darbhanga') #My name is Om. 
                                              #I am from darbhanga ,  \n this is a escape charater that put in next line

#next
x = 'this is a string'
y = "this is also a string"
z = '''first line
second line
third line'''
print(x) #this is a string
print(y) #this is also a string
print(z) #'''this command is used for if a sentence is in next line even than there will no error

#next
#String Methods
x='pytHoN sTrIng MEthOdS'
print(x.lower()) #python string methods
print(x.upper()) #PYTHON STRING METHODS
print(x.capitalize()) #Python string methods
print(x.title()) #Python String Methods
print(x.swapcase()) #PYThOn StRiNG meTHoDs

#next
x = 'python'
print(x.islower()) #true
x = 'Python'
print(x.islower()) #false
x = 'PYTHON'
print(x.isupper()) #true
x = 'PyThOn'
print(x.isupper()) #false
x = 'Python String Methods'
print(x.istitle()) #true
x = 'Python string methods'
print(x.istitle()) #false

#next
x = '123'
print(x.isdigit()) #ture
x = '123abc'
print(x.isdigit()) #false
x = 'abc'
print(x.isalpha()) #ture
x = 'abc123'
print(x.isalpha()) #false
x = 'abc123'
print(x.isalnum()) #true
x = 'abc123!@#'
print(x.isalnum()) #false

#next
x = '-----python-----'
print(x.strip('-')) #python
print(x.lstrip('-')) #python-----
print(x.rstrip('-')) #-----python

#next
x = 'Python'
print(x.startswith('P')) #true
print(x.startswith('p')) #false
print(x.endswith('n')) #true
print(x.endswith('N')) #false

#next
x = "Python String Methods"
print(x.count("t")) #3
print(x.count("s")) #1
print(x.index("t")) #2
print(x.index("s")) #20
x = x.replace("S", "s")
x = x.replace("M", "m")
print(x) #Python string methods

#next










