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
#find the total prfit/loss of each trader working in a trading firm. Information regarding number of traders and number of transactions is unknown
empID = input('Enter Employee ID: ')
while(empID != '-1'):
  trade = int(input('Enter the trade amount: '))
  profit_loss = 0
  while(trade != 0):
    profit_loss = profit_loss + trade
    trade = int(input('Enter the trade amount: '))
  print(f'Profit/loss for employee {empID} is {profit_loss}')
  empID = input('\nEnter Employee ID: ')

# Enter Employee ID: KL_343
# Enter the trade amount: 5678
# Enter the trade amount: 78909
# Enter the trade amount: -6789
# Enter the trade amount: 0
# Profit/loss for employee KL_343 is 77798

#next
#find the day wise total rainfall for the entered duration of time e.g. week, month, etc.

days = int(input("Enter the number of days: "))
for i in range(1, days+1):
  total = 0
  rainfall = int(input("Enter the rainfall: "))
  while(rainfall != -1):
    total = total + rainfall
    rainfall = int(input("Enter the rainfall: "))
  print("Total rainfall for day {0} is {1}".format(i, total))

# Enter the number of days: 88
# Enter the rainfall: 990
# Enter the rainfall: 098
# Enter the rainfall: 09899
# Enter the rainfall: 09988
# Enter the rainfall: -1
# Total rainfall for day 1 is 20975

#next
#find the length of longest word from the set of words entered by the user
word = input("Enter the word: ")
maxLen = 0
while(word != '-1'):
  count = 0
  for letter in word:
    count = count + 1
  if(count > maxLen):
    maxLen = count
  word = input("Enter the word: ")
print("The length of longest word is %s" %maxLen)

# Enter the word: om
# Enter the word: kumar
# Enter the word: thakur
# Enter the word: -1
# The length of longest word is 6

# break, continue and pass
email = input("Enter your email: ")
for c in email:
  if(c == "@"):
    break
  print(c, end =" ")
#  print(c) 

# Enter your email: omkumar@gmail.com
# o m k u m a r

# next
email = input("Enter your email: ")
for c in email:
  if(c == "@"):
    print("")
    continue
  print(c, end =" ")
 # print(c) 

# Enter your email: omkumar@gmail.com
# o m k u m a r 
# g m a i l . c o m

#next
for x in range(11):
  if(x% 3 == 0 ):
    print(x)
  else:
    pass

# 0
# 3
# 6
# 9

#GrPA 1
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while (n != 0): # the terminal condition
        total += n # add n to the total
        n = int(input()) # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input()
        if line == 'END': # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity), int(price) # convert to ints
        total_price = total_price + (quantity * price) # accumulate the total price
    print(total_price)

elif task == "only_ed_or_ing":
    word = input()
    while(word != 'STOP'):
        if ((word.endswith('ed')) or (word.endswith('ED')) or (word.endswith('ing')) or (word.endswith('ING'))):
            print(word)
        else:
            pass
        word = input()

elif task == "reverse_sum_palindrome":
    n = int(input())
    while(n != -1):
        if n > 0:
            reverse = int((str(n))[::-1])
            sum = n + reverse
            reverse_sum = int((str(sum))[::-1])
            if (sum == reverse_sum):
                print(n)
            else:
                pass
        else:
            pass
        n = int(input())

elif task == "double_string":
    line = input()
    while(line != ''):
        repeatedTwice = line * 2
        print(repeatedTwice)
        line = input()

elif task == "odd_char":
    word = input()
    while(word != word.endswith('.')):
        odd_char = word[::2]
        print(odd_char, end = ' ')
        word = input()

elif task == "only_even_squares":
    num = input()
    while(num != 'NAN'):
        num = int(num)
        square = num ** 2
        if (square % 2 == 0):
            print(square)
        else:
            pass
        num = input()

elif task == "only_odd_lines":
    new_line = ''
    line = input()
    while(line != 'END'):
        new_line = new_line + line + ' '
        line = input()
    split_line = new_line.split()
    odd_line = split_line[::2]
    reverse_odd_line = odd_line[::-1]
    reversed_line = '\n'.join(reverse_odd_line)
    print(reversed_line)

#GrPA 2
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1
    for i in range (1 , n+1):
       result *= i

    print(result)


elif task == 'even_numbers':
    n = int(input())
    for i in range (0 , n +1 , 2):
        print(i)

elif task == 'power_sequence':
    n = int(input())
    result = 1
    for i in range(n):
        print(2**i)


elif task == 'sum_not_divisible':
    n = int(input())
    sum = 0
    for i in range(1 , n):
        if (i % 4 != 0 and i % 5 != 0 ):
            sum += i
    print(sum)

elif task == 'from_k':
    n = int(input())
    k = int(input())
    count = 0
    for i in range (k,0,-1):
        str_i = str(i)
        if "5" not in str_i and '9' not in str_i and i%2!=0 :
            print(str_i[::-1])
            count += 1
            if count == n :
                break

elif task == 'string_iter':
    n = input()
    prev = 1
    for i in range(len(n)):
        curr = int(n[i])
        print(curr * prev)
        prev = curr

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input
    for i in lst:
        print(f'{i} - type: {type(i)}')

else:
    print("Invalid")

#GrPA 3
task = input()

if task == 'permutation':
    s = input()
    for i in s:
        for j in s:
            if (i != j):
                print(f'{i}{j}')

elif task == 'sorted_permutation':
    s = input()
    for i in s:
        for j in s:
            if ((i != j) and (i < j)):
                print(f'{i}{j}')

elif task == 'repeat_the_repeat':
    n = int(input())
    for i in range(1, n + 1):
        repeat_the_repeat = 0
        for j in range(1, n + 1):
            repeat_the_repeat = (repeat_the_repeat * 10) + j
        print(repeat_the_repeat)

elif task == 'repeat_incrementally':
    n = int(input())
    if (n > 0):
        repeat_incrementally = 0
        for i in range(1, n + 1):
            repeat_incrementally = (repeat_incrementally * 10) + i
            print(repeat_incrementally)

elif task == 'increment_and_decrement':
    n = int(input())
    if (n > 0):
        increment = ''
        for i in range(1, n + 1):
            increment = increment + str(i)
            decrement = increment[-2::-1]
            increment_and_decrement = increment + decrement
            print(increment_and_decrement) 

#GrPA 3
task = input()

if task == 'permutation':
    s = input()
    for i in s:
        for j in s:
            if (i != j):
                print(f'{i}{j}')

elif task == 'sorted_permutation':
    s = input()
    for i in s:
        for j in s:
            if ((i != j) and (i < j)):
                print(f'{i}{j}')

elif task == 'repeat_the_repeat':
    n = int(input())
    for i in range(1, n + 1):
        repeat_the_repeat = 0
        for j in range(1, n + 1):
            repeat_the_repeat = (repeat_the_repeat * 10) + j
        print(repeat_the_repeat)

elif task == 'repeat_incrementally':
    n = int(input())
    if (n > 0):
        repeat_incrementally = 0
        for i in range(1, n + 1):
            repeat_incrementally = (repeat_incrementally * 10) + i
            print(repeat_incrementally)

elif task == 'increment_and_decrement':
    n = int(input())
    if (n > 0):
        increment = ''
        for i in range(1, n + 1):
            increment = increment + str(i)
            decrement = increment[-2::-1]
            increment_and_decrement = increment + decrement
            print(increment_and_decrement) 

#GrPA 4
# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None 
all = None
min = None 

task = input()


if task == 'factors':
    n = int(input())
    if (n > 0):
        for i in range(1, n + 1):
            if (n % i == 0):
                print(i)

elif task == 'find_min':
    n = int(input())
    min = 99999999999999999
    num = int(input())
    if (n > 1):
        while (n > 1):
            if num < min:
                min = num
            num = int(input())
            n -= 1
    else:
        min = num
    print(min)

elif task == 'prime_check':
    num = int(input())
    flag = False
    if (num > 0):
        if (num == 2):
            flag = True
        else:
            for i in range(3, num + 1):
                for j in range(2, i):
                    if (i % j == 0):
                        flag = False
                        break
                    else:
                        flag = True
        print(flag)

elif task == 'is_sorted':
    s= input()
    flag = True
    for i in range(len(s) - 1):
        if (s[i] > s[i + 1]):
            flag = False
            break
    print(flag)

elif task == 'any_true':
    n = int(input())
    num = int(input())
    flag = False
    while(n > 1):
        if(num % 3 == 0):
            flag = True
        n -= 1
        num = int(input())
    print(flag)

elif task == 'manhattan':
    direction = input()
    x_distance, y_distance = 0, 0
    while (direction != 'STOP'):
        if (direction =='LEFT'):
            x_distance -= 1
        elif (direction == 'RIGHT'):
            x_distance += 1
        elif (direction == 'UP'):
            y_distance += 1
        elif (direction == 'DOWN'):
            y_distance -= 1
        x, y = abs(x_distance - 0), abs(y_distance - 0)
        manhattan_distance = x + y
        direction = input()
    print(manhattan_distance)













