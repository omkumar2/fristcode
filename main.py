#week 1

print("Hello, type your name :")
n=str(input())
print("Which place are you in?")
p=str(input())
print("Hello",n,"How is the weather in",p,"?")
print("what is your age?")
age=int(input())
print("good know you are ",age,"years old")

#this both are same

n=str(input("Hello, type your name :"))
p=str(input("Which place are you in?"))
print("Hello",n,"How is the weather in",p,"?")
age=int(input("what is your age?"))                                      
print("good know you are ",age,"years old")

#area of circle
r = int(input("Enter the radius of the circle: "))
area = 3.14*r*r
print("Area of the circle with radius",r,"is",area)

#list

l=[10,20,30]
print(l[0])
print(l[1])
print(l[2])

print(type(l[2]))#<class 'int'>
print(type(l)) #this show console -- <class 'list'>

# data type 1
l=[10,20,30]
n=10
r=6.3
o="om kumar"

print(type(l)) #<class 'list'>
print(type(n)) #<class 'int'>
print(type(r)) #<class 'float'>
print(type(o)) #<class 'str'>

#other data type

b1 = True
b2 = False
print(type(b1)) #<class 'bool'>
print(type(b2)) #<class 'bool'>

#data type 2

a=int(5.7)
b=int("10")

print(a, type(a)) #5<class 'int'>
print(b, type(b)) #10 <class 'int'>

c=float(5)
d=float("1.4")

print(c, type(c)) #5.0 <class 'float'>
print(d, type(d)) #1.4 <class 'float'>

e=str(5.3)
f=str(1)

print(e, type(e)) #5.3 <class 'str'>
print(f, type(f)) #1 <class 'str'>

g=bool(1)
h=bool(0)
i=bool(-1)

print(g, type(g)) #True <class 'bool'>
print(h, type(h)) #False <class 'bool'>
print(i, type(i)) #True <class 'bool'>

j=bool(10.5)
k=bool(0.0)
l=bool(-10.6)

print(j, type(j)) #True <class 'bool'
print(k, type(k)) #False <class 'bool'>
print(l, type(l)) #True <class 'bool'>


a=bool("india")
b=bool("10")
c=bool("-10.5")
d=bool("0")
e=bool("")

print(a,type(a)) #True <class 'bool'>
print(b,type(b)) #True <class 'bool'>
print(c,type(c)) #True <class 'bool'>
print(d,type(d)) #True <class 'bool'>
print(e,type(e)) #False <class 'bool'>

#Operators and Expressions 1

a=12
b=3.3
n=a+b
print(n) #15.3

a='jay'
b='om'
n=a*b
print(n) #error

a='jay'
b='om'
n=a+b
print(n) #jayom

a=[1,2,3]
b=[7,9,12]
n=a+b
print(n) #[1,2,3,9,12]

n=10+13*2
#my guess is n will be 46.
#the expected answer was incorrect. the correct answer is 36. That is due to what is called the operator precedence.
print(n)

n=((10+13)*2) # is 46
print(n)

#introduation to strings

s="coffee"
t="bread"
print(s[1]) #it will show c
#next
s="coffee"
t="bread"
print(s[1:4])#it will off
#next
s="0123456789"
a=s[5]
b=s[6]
print(a) #5
print(b) #6
print(a+b) #56
#next
s="0123456789"
a=int(s[5])
b=int(s[6])
print(a) #5
print(b) #6
print(a+b) #11

#more about string

s="good"
print(s[0]*5) #ggggg
#next
x="india"
print(x== "india") #true
print(x== "India") #false
#next
print("apple" > "one" ) #false
print( "four" < "ten") #true
print( 4 < 10) #true
print("ab" < "az") #true
print("abcdef" < "abcde") #true
#next
s="python"
print(s[-1]) #n
print(s[-2]) #o
print(s[-3]) #h
print(s[-4]) #t
print(s[-5]) #y
print(s[-6]) #p
#next
s="hkgjhkgkkgjkjdghfuu"
print(len(s)) #19  = this is number of letter in line
print(s[18]) #u
print(s[19]) #error
#next

 #Operators and Expressions 2

#arithmetic operators(+,-,*,/,//,%,**)
print("addition",2+3) #addition 5
print("subtraction",9-1) #subtraction 8
print("multiplication",5*4) #multiplication 20
print("division",7/3) #division 2.3333333333333335
print("floor division",7//3) #floor division 2
print("modulus",7%3) #modulus 1
print("exponential",6**2) #exponential 36

#relational operators(>,<,>=,<=,==,!=)
print(5>10) #false
print(10>5) #true
print(5<10) #true
print(10<5) #false
print(5>=5) #true
print(5<=5) #true
print(5==5) #true
print(5!=5) #false

#logical operators (and, or, not)
print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false

print(True or True) #true
print(True or False) #true
print(False or True) #true
print(False or False) #false

print(not(True)) #false
print(not False) #true

#GrPA 1

output1 = a+b # int: sum of a and b
output2 = 2*(a+b) # int: twice the sum of a and b
output3 = abs(a-b) # int: absolute difference between a and b
output4 = abs((a+b) - (a*b)) # int: absolute difference between sum and product of a and b

# Find discounted price given price and discount_percent
# input variables : price: int, discount_percent: float
discounted_price = (1-discount_percent/100)*price # float

# Round the discounted_price
rounded_discounted_price = round(discounted_price) # int

# Find hrs and mins given the total_mins
# input variables : total_mins
hrs = total_mins//60 # int: hint: think about floor division operator
mins = total_mins%60 # int

#GrPA 2

output1 = a+b # int: sum of a and b
output2 = 2*(a+b) # int: twice the sum of a and b
output3 = abs(a-b) # int: absolute difference between a and b
output4 = abs((a+b) - (a*b)) # int: absolute difference between sum and product of a and b

# Find discounted price given price and discount_percent
# input variables : price: int, discount_percent: float
discounted_price = (1-discount_percent/100)*price # float

# Round the discounted_price
rounded_discounted_price = round(discounted_price) # int

# Find hrs and mins given the total_mins
# input variables : total_mins
hrs = total_mins//60 # int: hint: think about floor division operator
mins = total_mins%60 # int

#GrPA 3

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.

s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id
# <eoi>

output1 = s[2] # str: get the third character of s

output2 = s[-4] # str: get the fourth last character of s

output3 = s[:3] # str: get the first 3 characters of s

output4 = s[::2] # str: get every second character of s

output5 = s[-3:] # str: get the last 3 characters of s

output6 = s[::-1] # str: get the reverse of s

course_term = int(course_code[3]) # int: get the term of the year as number from course_code
course_year = int(course_code[:2]) # int: get the year as two digit number from course_code

#GrPA 4

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>

output1 = word1 + " " + word2 # str: join word1 and word2 with space in between

output2 = word1[:4] + "-" + word2[-4:] # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between

output3 = word3 + " " + str(n1) # str: join the word3 and n1 with a space in between

output4 = "-"*50 # str: just the hypen "-" repeated 50 times

output5 = "-"*n2 # str: just the hypen "-" repeated n2 times

output6 = str(n1)*n2 # str: repeat the number n1, n2 times

are_all_words_equal = word1 == word2 == word3 # bool: True if all three words are equal

is_word1_comes_before_other_two = word1 < word2 and word1 < word3 # bool: True if word1 comes before word2 and word3 assume all words are different

has_h = 'h' in word1 # bool: True if word1 has the letter h

ends_with_a = word1.endswith('a') or word1.endswith('A') # bool: True if word1 ends with letter a or A

has_the_word_python = 'python' in sentence # bool: True if the sentence has the word python

#GrPA 5

age = int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = str(day)+"/"+str(month)+"/"+str(year+5) # str: fifth birthday formatted as day/month/year 

last_birthday = str(day)+"/"+str(month)+"/"+str(year+age) # str: last birthday formatted as day/month/year

month += 10
month, year = (month-1)%12+1, year+(month-1)//12
tenth_month = str(day)+"/"+str(month)+"/"+str(year) # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month,fifth_birthday,last_birthday, sep=", ")

weight = float(input()) # float: Read a number as float from stdin(Standard input)

kg = int(weight)  # Get the integer part (kg)
grams = int((weight - kg) * 1000)  # Get the fractional part converted to grams

weight_readable = str(kg)+" kg "+str(grams)+" grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)















