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
print("We are from \"IIT\" Madras") #We are from "IIT" Madras
print('We are from "IIT" Madras') #We are from "IIT" Madras

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

#An Interesting Cipher: More on Strings

alpha='abcdefghijklmnopqrstuvwxyz'

i=1
print(alpha[i]) #b
print(alpha[i+1]) #c
print(alpha[i+2]) #d

#next
alpha='abcdefghijklmnopqrstuvwxyz'

i=24
print(i%26) #24
print(alpha[i%26]) #y
print(alpha[(i+1)%26]) #z
print(alpha[(i+2)%26]) #a

#next
alpha='abcdefghijklmnopqrstuvwxyz'

o='om kumar'
#i expect to output tvebstibo
t=''

print(alpha.index(o[0])) #14
print(((alpha.index(o[0]))+1)%26) #15
print(alpha[((alpha.index(o[0]))+1)%26]) #p
t=t+(alpha[((alpha.index(o[0]))+1)%26]) 
print(t) #p

i=0
k=2
t=t+(alpha[(((alpha.index(o[i]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+1]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+2]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+4]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+5]))+k)%26)])
t=t+(alpha[(((alpha.index(o[i+6]))+k)%26)])
print(t) #pqomwoct

#Introduction to the if statement

#if condition
#let us consider the movie "Avengers". This is a 13+ movie.
print("Please enter your date of birth")
birth_year=int(input())

current_year=2025

age=current_year-birth_year
if(age<13):
  print("You are under age, you cannot watch this movie.")
  print("Wait until you are old enough to watch this movie.")
else:  
  print("you are old enough to watch avengers, enjoy!")
  print("Don't forget to watch the sequels and prequels.")

print("Have a nice time")

# Please enter your date of birth
# 2006
# you are old enough to watch avengers, enjoy!
# Don't forget to watch the sequels and prequels.
# Have a nice time

# Tutorial on if, else and else-if (elif) conditions

#find wether the number is even or odd
num = int(input("Enter a number: "))

if(num % 2 == 0) :
  print("The number is even")
else:
  print("The number is odd")
# Enter a number: 5
# The number is odd

#next
#find wether the given number ends with 0 or 5 or any other number
num = int(input("Enter a number: "))
if(num % 5 == 0):
  if(num % 10 == 0):
    print('0')
  else:
    print('5')
else:
  print("other") 
#Enter a number: 4
#other

#next
#find the grade of student based on the given marks from 0 to 100
marks = int(input("Enter your marks: "))

if(marks>=90 and marks<100):
  print("A")
elif(marks>=80 and marks<90):
  print("B")
elif(marks>=70 and marks<80):
  print("C")
elif(marks>=60 and marks<70):
  print("D")
elif(marks>=0 and marks<0):
  print("E")
else:
  print("Invalid input")
# Enter your marks: -2
# Invalid input

#Different ways to import a library

import math
print(math.log(10)) #2.302585092994046
print(math.sin(90)) #0.8939966636005579
print(math.sqrt(16)) #0.4
print(math.factorial(5)) #120
print(math.pow(10,3)) #1000

#next
import random
print(random.random()) # Any number you want 0 to 10
print(random.randrange(1,6)) #Any number you want 1 to 6

#next
dice1=(random.randrange(1,6))
dice2=(random.randrange(1,6))
total=dice1+dice2
print("your pair of dice is:",total) #Any number you want 1 to 12

#next
#let us simulate a coin toss.
import random
a=random.random()
if(a<.5):
  print("Heads")
else:
  print("Tails")  # This Is a Random head and tail

#Different ways to import a library

import calendar
print(calendar.month(2026,5)) #it show entire month
print(calendar.calendar(2026)) #it show Entire year

from calendar import *
print(calendar(2026)) 
print(month(2026,5)) #in this  i ot need to write calendar

#GrPA 1

x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`
x1,x2 = x2,x1

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 
y1,y2,y3 = y2,y3,y1

# create a new variable `a` with the value of `z`
a = z

# delete the variable `z`
del z

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)

#GrPA 2

# A single quote ' and a double quote "
output1 = 'A single quote \' and a double quote "'

# A forward slash / and a backward slash \
output2 = 'A forward slash / and a backward slash \\' 

# Three single quotes ''' and three double quotes """
output3 = "Three single quotes ''' and three double quotes \"\"\"" 

# Double forward slash // and Double backward slash \\
output4 = "Double forward slash // and Double backward slash \\\\"

#GrPA 3

# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if new_word[-3:] == "ing" :
    new_word = new_word[:-3]

# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here

if continuous_tense:
    new_word=new_word+"ing"

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age<18:
    age_group = "Child"
else:
    age_group = "Adult"

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block

if is_member:
    applicant_type = age_group+" "+"Member"
else:
    applicant_type = age_group+" "+"Non-member"

# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if color_code=="R":
    color = "red"
elif color_code == "G":
        color = "green"
elif color_code == "B":
    color = "blue"
else:
    color = "black"

is_time_valid = 0<int(time[:2])<=12 # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = int(time[:2])%12 + (time[-2:] == "PM") * 12

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here

if not is_time_valid:
    time_of_day = "Invalid"
elif 0 <= time_in_hrs < 6:
    time_of_day = "Night"
elif 6<= time_in_hrs < 12:
    time_of_day = "Morning"
elif 12<= time_in_hrs < 18:
    time_of_day = "Afternoon"
elif 18<= time_in_hrs < 24: # you could also use else here.
    time_of_day = "Evening"

#GrPA 4

# Take operation name from input
operation = input()

if operation == "odd_num_check":
    # Odd number checker
    number = int(input())
    if number % 2 == 0:
        print("no")
    else:
        print("yes")

elif operation == "perfect_square_check":
    # Perfect square checker
    number = int(input())
    if int(number**0.5)**2 == number:
        print("yes")
    else:
        print("no")

elif operation == "vowel_check":
    # Vowel checker
    string = input().lower()
    if ("a" in string or "e" in string or "i" in string or "o" in string or "u" in string) :
        print("yes")
    else:
        print("no")

elif operation == "divisibility_check":
    # Divisibility checker
    number = int(input())
    if number % 2 == 0:
        if number % 3 == 0:
            print("divisible by 2 and 3")
        else:
          print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif operation == "palindrominator":
    # Palindrominator
    string = input()
    palindrome = string + string[-2::-1]
    print(palindrome)

elif operation == "simple_interest":
    # Simple interest calculator
    principal_amount = float(input())
    n_years = int(input())
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    simple_interest = principal_amount * interest_rate * n_years
    print(int(simple_interest))

else:
    print("Invalid Operation")

#GrPA 5

main_dish = input()
time_of_day = int(input())
has_voucher = input() == "True"
is_card_payment = input() == "True"

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else:
    print("Invalid main dish")
    exit()

if time_of_day >= 12 and time_of_day <= 15:
    discount = 0.15 * cost
    total_cost = cost - discount
else:
    total_cost = cost

if has_voucher:
    total_cost *= 0.9  # Apply voucher discount

if is_card_payment:  # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost += service_charge

print(f"{total_cost:.02f}")










