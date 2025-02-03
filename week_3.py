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

#Enter the number: -1234
#-4321

#next








































