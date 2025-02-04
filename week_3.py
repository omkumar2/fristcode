#week_3

#Introduction to while loop

print("when did india get its independence (year)?")
year=int(input())

if(year==1947):
  print("hip hip hurray. you got that right!")
else:
  print("comeon dont you know even this?")
  print("that's ok, i will let you attempt this once more")
  print("when did india get its independence?")
  year=int(input())
  if(year==1947):
    print("you got it!")
  else:
    print("failed in your second attempt too? grrrr...")

#this code is write by while loop
print("when did india get its independence (year)?")
year=int(input())

while(year!=1947):
    print(year,"you got this wrong. enter once again")
    year=int(input())
print("woww...you got it right")

#while works like this:
   #while <condition>
   #write whatever you want here
   #write whatever you want here
   #write whatever you want here

#  While to Compute Factorial

#let us find the factorial of a number

print("Enter a number:")
n=int(input())
#n=5
#1*2*3*4*5
i=1
answer=1
while(i<=n):
   answer=answer*i
   i=i+1
print(answer)

# Tutorial on while loop

#let us find the factorial of a number
num=int(input("Enter a number:"))

fact=1
if(num<0):
  print("Not defined")
else:
  while(num > 0):
    fact=fact*num
    num=num-1
print(fact)

#next
#find the number of digits in the given number
num = abs(int (input ('Enter s number: ')))
digits = 1
while(num > 9) :
  num = num // 10
  digits = digits + 1
print(digits)

#Enters number: 677
#3

#next
#reverse the digits in the given number
num = int(input("Enter the number: "))  #num = abs(int(input("Enter the number: ")))   it can be do of negative number
rev = num % 10
num = num // 10
while (num > 0):
  r = num % 10
  num = num // 10
  rev = rev * 10 + r
print(rev)
#Enter the number: 678
#876

#or
num = int(input("Enter the number: "))
absNum =abs(num)
if(num > 0):
    rev = num % 10
    num = num // 10
    while(num > 0):
        r = num % 10
        num = num // 10
        rev = rev * 10 + r
    print(rev)
else:
    rev = absNum % 10
    absNum = absNum // 10
    while(absNum > 0):
        r = absNum % 10
        absNum = absNum // 10
        rev = rev * 10 + r
    print(rev - 2 * rev)

#or
num = int(input("Enter the number: "))
absNum =abs(num)
rev = absNum % 10
absNum = absNum // 10
while(absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r
if(num >= 0):
    print(rev)
else:
    print(rev - 2 * rev)

#Enter the number: -1234
#-4321

#next
rev = absNum % 10
absNum = absNum // 10
while(absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r
if(num < 0):
    rev = rev - 2 * rev
  
if(num == rev):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Enter the number: 12321       Enter the number: 456
#Palindrome                    Not a Palindrome

# Introduction to for loop

#An example of a for loop

for i in range(4):
 print(i,"Hello India")
 print("*************")
 print("@@@@@@@@@@@@@")
 
# 0 Hello India
# *************
# @@@@@@@@@@@@@
# 1 Hello India
# *************
# @@@@@@@@@@@@@
# 2 Hello India
# *************
# @@@@@@@@@@@@@
# 3 Hello India
# *************
# @@@@@@@@@@@@@

#next
#An example of a for loop
print("Enter a number:")
n=int(input())

for i in range(n):
  if (i%2==0):
    print(i,"Hello India")
  else:
    print(i,"Hi World")
    
# Enter a number:
# 4
# 0 Hello India
# 1 Hi World
# 2 Hello India
# 3 Hi World

# for loop to add the first n numbers

#Adds frist 10 integer numbers
num=int(input("Enter a number:"))

ans=0
for i in range(num):
  ans=ans+i
print("The answer is",ans)

# nter a number:11
# The answer is 55

#for loop for multiplication tables

for i in range(1,5):
  print("2 X ", i, "=", 2*i)

# 2 X  1 = 2
# 2 X  2 = 4
# 2 X  3 = 6
# 2 X  4 = 8

#More on range and for loop without range

for x in range(1,11):
  if(x % 2 != 0):
   print(x)

#next
for x in range(9, -1, -1):
  print(x)   

# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
  
#here 1 is the starting number, 11 is the ending number and 2 is the step size

#next
country = "India"
for letter in country:
  print(letter)

# I
# n
# d
# i
# a

# Formatted Printing

for x in range( 10):
  print(x, end = " ")  # 0 1 2 3 4 5 6 7 8 9

#next
d = 3
m = 2
y = 2025
print("todays date is", end = ' ')
print(d, m, y, sep = "-") # todays date is 3-2-2025

#next
num = int(input("enter a number: "))
for i in range(1, 11):
  #print(num, 'x', i, '=', num*i)
  #print(f'{num} x {i} = {num*i}')
  #print('%d X %d = %d' %(num, i, num*i))
  print('{0} X {1} = {2}'.format(num, i, num*i))

# enter a number: 5
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50

#next
pi = 22 / 7
print(f'Value of Pi = {pi}') #Value of Pi = 3.142857142857143
print('Value of Pi = {0}'.format(pi)) #Value of Pi = 3.142857142857143
print('Value of Pi = %f' % (pi)) #Value of Pi = 3.142857

print(f'Value of Pi = {pi:.2f}') #Value of Pi = 3.14
print('Value of Pi = {0:.2f}'.format(pi)) #Value of Pi = 3.14
print('Value of Pi = %.4f' % (pi)) #Value of Pi = 3.1428

#next
print('{0:4d}'.format(1))
print('{0:5d}'.format(11))
print('{0:4d}'.format(111))
print('{0:5d}'.format(1111))

# 1
#    11
#  111
#  1111

#Tutorial on for loop and difference between while loop and for loop

#find the factorial of the given number
num = int(input("Enter a number: "))
fact = 1
if num < 0:
  print("Factorial does not exist for negative numbers")
else:
  for i in range(1, num + 1):
    fact = fact * i
  print("The factorial of", num, "is", fact)
  #   for i in range(num, 1, -1):
  #   fact = fact * i
  # print("The factorial of", num, "is", fact)

# Enter a number: 5
# The factorial of 5 is 120
#find the number of digits in the given number
num = abs(int(input("Enter a number: ")))
strNum = str(num)
digits = 0
for c in strNum:
  digits = digits + 1
print(digits)
# lentgh = len(str(num))
# print(lentgh)

# Enter a number: 4567
# 4

#next
#rerver the digits in the given number
num = int(input("Enter a number: "))
absStrNum = str(abs(num))
rev = ""
for c in absStrNum:
  rev = c + rev
if (num >= 0):
  print(rev)
else:
  print("-" + rev)

# Enter a number: 7890
# 0987

#next
#find whether the entered number is palindrome or not
num=int(input("Enter a number: "))
absStrNum = str(abs(num))
rev = ''
for c in absStrNum:
  rev = c + rev
if num < 0:
  rev = '-' + rev
if num == int(rev):
  print("Palindrome")
else:
  print("Not a Palindrome")

# Enter a number: 123
# Not a Palindrome

#  Nested for loop

s="VIBGYOR"

for i in range(5):
  print(s[i])
 
# V
# I
# B
# G
# Y

#next
#two brothers sharath and tanmay
s='VIBGYOR'
t='VIBGYOR'
#example of nested for loop
count=0
for i in range(7):
  for j in range(7):
    print(i,j,s[i],s[j])
    count=count+1

print("the total ways in which the two brothers can wear 7 different colours:",count)

#i=0 and j=0 print VV
#i=0 and j=1 print VI
#i=0 and j=2 print VB
#i=0 and j=3 print VG
#....
#i=0 and j=6 print VR
#i=1 and j=0 print IV

#Tutorial on nested loops

#find all prime numbers less than the entered number
num = int(input("Enter a number: "))
if (num > 2):
  print(2, end = ' ')
for i in range(3, num):
  flag = False
  for j in range(2, i):
    if (i % j == 0):
      flag = False
      break
    else:
      flag = True
  if (flag):
    print(i, end = ' ')

#next























