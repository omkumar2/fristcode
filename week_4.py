
#Warmup with Lists

l=[1,2,3,6,77]
print(l) #[1, 2, 3, 6, 77]
l.append(1045)
print(l) #[1, 2, 3, 6, 77, 1045]
l.append(2)
print(l) #[1, 2, 3, 6, 77, 1045, 2]
l.remove(77)
print(l) #[1, 2, 3, 6, 1045, 2]
l.remove(2)
print(l) #[1, 3, 6, 1045, 2]

#next
l=[]
l.append(1)
l.append(2)
l.append(3)
print(l) #[1, 2, 3]
x=[]
x.append(l)
print(x) #[[1, 2, 3]]
m=[10,20,30]
x.append(m)
print(x) #[[1, 2, 3], [10, 20, 30]]
t=[]
t.append(x)
print(t) #[[[1, 2, 3], [10, 20, 30]]]
t.append([100,101,102])
print(t) #[[[1, 2, 3], [10, 20, 30]], [100, 101, 102]]
print(t[0]) #[[1, 2, 3], [10, 20, 30]]
print(t[1]) #[100, 101, 102]
M=[]
M.append([1,2,3]) 
M.append([4,5,6])
M.append([7,8,9])
print(M) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M[0]) #[1, 2, 3]
print(M[0][0]) #1
print(M[0][1]) #2

#Lists and Sets

l=list(range(10))
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([5]) #[5]
l.append("om kumar")
l.append("code om")
l.append(2.23) 
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'om kumar', 'code om', '2.23']
print(5 in l) # true
print(-1 in l) # false
print("om" in l) #false
print("code om" in l) #true
print(2.230 in l) # false or true
l=list(range(100000))

print(l[13]) #13
print("code om" in l)  # false
x=[1,4,5,6,4,8,5,3,7,9,5,9,0]
print(x) #[1, 4, 5, 6, 4, 8, 5, 3, 7, 9, 5, 9, 0]

y={1,4,5,6,4,8,5,3,7,9,5,9,0}
print(type(x)) #<class 'list'>
print(type(y)) #<class 'set'>
print(y) #{0, 1, 3, 4, 5, 6, 7, 8, 9}

print(8 in y) #true
print(9 in y) #true
print(10 in y) #false

#next
l=list(range(100000))
s=set(range(10))
print(s) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

x=list(range(10))
print(x) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s=set(range(10000000))
print(0 in l) #true
print(1 in l) #true
print(-2 in l) #false
print(0 in s) #true
print(1 in s) #true
print(-2 in s) #false
print("omkumar" in s) #false

#next



#next
import sys
l=[]
l1=[0]
l2=[0,1]

print(sys.getsizeof(l)) #56
print(sys.getsizeof(l1)) #64
print(sys.getsizeof(l2)) #72

x=list(range(100))
s=set(range(100))
print(sys.getsizeof(x)) #856
print(sys.getsizeof(s)) #8408

print(x[2]) #2
print(s[0]) #'set' object is not subscriptable            error

z=('om kumar','jay', 'antra', 'chubul')
print('om kumar' in z) #true
print('om' in z) #false
z = z.__add__(('code','python'))  # Assign the result to zn'))  # Assign the result to z
print(z) #('om kumar', 'jay', 'antra', 'chubul', 'code', 'python')
print(z[0]) #om kumar

a=[1,2,3,3,8,9,6,4]
b={3,3,4,6,7,7,8,88}
print(a) #[1, 2, 3, 3, 8, 9, 6, 4]
print(b) #{3, 4, 6, 7, 8, 88}

# Tuples

l=[5,7,19,10,4]
l.append(100)
print(l) # [5, 7, 19, 10, 4, 100]
l.remove(7)
print(l) # [5, 19, 10, 4, 100]
t=(2,7,18,64,101,108,65)
print(t) # (2, 7, 18, 64, 101, 108, 65)
t.remove(101) #it will through error
t.append(100) #it will through error
print(t[0]) #2
print("A tuple is unchangeable") #A tuple is unchangeable
print("A list can changed") # A list can changed 

l=list(range(10))
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t=tuple(range(10))
print(t) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print("l is flexible but t is not") #l is flexible but t is not
import string
s=string.ascii_letters
print(s) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
s=string.ascii_lowercase
print(s) # abcdefghijklmnopqrstuvwxyz
s=string.ascii_uppercase
print(s) # ABCDEFGHIJKLMNOPQRSTUVWXYZ

s=string.ascii_letters
print(s) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
s=set(s) 
print(s) # ('v', 'G', 'm', 'C', 'g', 'n', 'h', 'k', 'b', 'e', 'a', 'r', 'J', 'Y', 'A', 'M', 'd', 'j', 'I', 'N', 'i', 'y', 'z', 'P', 'R', 'F', 's', 'T', 'l', 'B', 'D', 'u', 'L', 'p', 'c', 'Z', 't', 'H', 'w', 'o', 'Q', 'W', 'x', 'E', 'X', 'V', 'f', 'S', 'U', 'q', 'O', 'K')

alpha=tuple(s)
print(alpha)# ('v', 'G', 'm', 'C', 'g', 'n', 'h', 'k', 'b', 'e', 'a', 'r', 'J', 'Y', 'A', 'M', 'd', 'j', 'I', 'N', 'i', 'y', 'z', 'P', 'R', 'F', 's', 'T', 'l', 'B', 'D', 'u', 'L', 'p', 'c', 'Z', 't', 'H', 'w', 'o', 'Q', 'W', 'x', 'E', 'X', 'V', 'f', 'S', 'U', 'q', 'O', 'K')
s=string.ascii_letters
alpha=tuple(list(s))
print(alpha) # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
print(list(s)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

x='sudarshan#%&^$indiaBharath()Karnataka$%punjab#tamilnadu'

r=[]
for p in l:
  if p  in alpha:
    r.append(p)

print(r) #[]

l=list(range(10))
t=tuple(range(10))
print(l.__sizeof__()) #120
print(t.__sizeof__()) #104

print("when we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple") #when we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple

#More on Lists

l1 = [1,2,3]
l2 = [10,20,30]
l12 = l1 + l2
l21 = l2 + l1
print(l12, l21) #[1, 2, 3, 10, 20, 30] [10, 20, 30, 1, 2, 3]

#next
l1= [0]*10
print(l1) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l2= [1,2,3]*5
print(l2) #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#next
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
print(l1 == l2) #true 
print(l2 == l3) #false
print(l2 < l3) #true

#next
print([1,2] < [2,1]) #true
print([] < [1,2,3]) #true
print([2,3] < [3]) #true
print([] < [1]) #true

#next
l = [1,2,4]
print(l) #[1,2,4]
l[2] = 3
print(l) #[1,2,3]

s= 'abce'
print(s[3]) #e
s[3] = 'd'
print(s) #'str' object does not support item assignment      or  error

#next
x=5
y=x
x=10
print(x,y) #10 5

l1=[1,2,3]
l2=l1
l1[0]=100
print(l1,l2) #[100, 2, 3] [100, 2, 3]

#next
l1=[1,2,3]
l2=list(l1)
l3=l1[:]
l4=l1.copy()

l2[0]=100
l3[1]=200
l4[2]=300

print(l1,l2,l3,l4) #[1, 2, 3] [100, 2, 3] [1, 200, 3] [1, 2, 300]

print(l1 is l2) #false
print(l1 is l3) #false
print(l1 is l4) #false
print(l1 is l5) #true

# function
def add(x):
  x = x + 1
  return x

x = 5
print(add(x)) #6
print(x) #5

def add(x):
  x.append(1)
  return x

x = [5]
print(add(x)) #[5,1]
print(x) #[5,1]

#next
l=[1,2,3]
print(l) #[1,2,3]

l.append(4)
print(l) #[1,2,3,4]

l.insert(2,9) # Insert 9 at index 2
print(l) #[1,2,9,3,4]

#next
l=[1,2,3]
print(l) #[1,2,3]

l.remove(2)
print(l) #[1,3]

l.pop(0) # Remove the element at index 0
print(l) #[3]

#next
l=[2,6,1,50,3,7,5]
l.sort()
print(l) #[1, 2, 3, 5, 6, 7, 50]

#next
l=[2,6,1,50,3,7,5]
l.reverse()
print(l) #[5, 7, 3, 50, 1, 6, 2]

# More on Sets

st={1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(st) #{1, 2, 3, 4, 5}
print(st[0]) #set' object is not subscriptable          or   error

#next
A={1, 3, 5}
B={1, 2, 3, 4, 5}
print(A.issuperset(B)) #false   

#next
A = {1, 2, 3}
B = {3, 4, 5}
c1 = A.union(B)
c2 = A | B
print(c1, c2) #{1, 2, 3, 4, 5} {1, 2, 3, 4, 5}

#next
A = {1, 2, 3}
B = {3, 4, 5}
c1 = A.intersection(B)
c2 = A & B
print(c1, c2) #{3} {3}

#next
A = {1, 2, 3}
B = {3, 4, 5}
c1 = A.difference(B)
c2 = A - B
print(c1, c2) #{1, 2} {1, 2}

#More on Tuples

t = 1, 2, 3
print(t, type(t)) #(1, 2, 3) <class 'tuple'>

x, y, z = t
print(x, y, z)  #1 2 3

#next
X = 5
Y = 10
X, Y = Y, X
print(X, Y) # 10 5

#next
l = [10]
print(l, type(l)) #[10] <class 'list'>

t = (10)
print(t, type(t)) #10 <class 'int'>

t = (10,)
print(t, type(t)) #(10,) <class 'tuple'>

#next
t = ([1, 2], ['a', 'b'])
t[0] = [10, 20]
print(t) #'tuple' object does not support item assignment       or   error

#next
t = ([1, 2], ['a', 'b'])
t[0][0] = 10
print(t) #([10, 2], ['a', 'b'])

#we can not modify "Tuple" but inside the "Tuple" we can modify the "list" 

# : List Comprehensions

a = 10
b = 20
'''
if a < b:
  small = a
else:
  small = b
''' #both code are same
small = a if a < b else b
print(small)  # 10

#next
a = 5
'''
while a > 0:
  print(a)
  #a = a - 1
  a -= 1
  '''  #the both code is same
while a > 0: print(a); a -= 1

# 5
# 4
# 3
# 2
# 1

#next
fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
'''
newList = []
for fruit in fruits:
  if "n" in fruit:
    newList.append(fruit.capitalize())
    ''' # again the code are same
newList = [fruit.capitalize() for fruit in fruits if "n" in fruit]
print(newList) # ['Mango', 'Banana', 'Orange', 'Pineapple', 'Watermelon']

# Introduction to Functions

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
'''
newList = []
for fruit in fruits:
  if "n" in fruit:
    newList.append(fruit.capitalize()) #capitalize() is used to capitalize the first letter of the string
'''
newList = [fruit.capitalize() for fruit in fruits if "n" in fruit]
print(newList)  #['Mango', 'Banana', 'Orange', 'Pineapple', 'Watermelon']

# Introduction to Functions

def add(a,b):
  ans=a+b
  print(ans)

add(1,3) #4

def sub(a,b):
  ans=a-b
  print(ans)

sub(10,8) #2

def discount(cost,d):
  ans=cost-(cost*(d/100))
  print(ans)

discount(100,8.3) #91.7

add(17,5)+sub(100,3)+discount(1500,7.5) #TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'    and it print 22 ,  97

#next
def add(a,b):
  ans=a+b
  return ans

a=2
b=15
ans=add(a,b)+10
ans=a+b+10
print(ans) #27

#next
def discount(cost,d):
  ans=cost-(cost*(d/100))
  return ans

print("Enter the cost price") #1000
c=int(input())
print("Enter the discount") #11
disc=int(input())
print("The final discounted price is:",discount(c,disc)) #The final discounted price is: 890.0


print("Enter the cost price") #1000
x=int(input())
print("Enter the discount") #11
y=int(input())
print("The final discounted price is:",discount(x,y)) #The final discounted price is: 890.0

#More Examples of Functions

#let write a few function on lists

def frist_element(l):
  return l[0]
x=[1,2,3]
print(frist_element(x)) #1

def second_element(l):
  return l[1]
print(second_element(x)) #2

#next
#let write a few function on lists

def list_min(l):
  mini=l[0]
  for i in range(len(l)):
    if(l[i]<mini):
      mini=l[i]
  return mini

def list_max(l):
  maxi=l[0]
  for i in range(len(l)):
    if(l[i]>maxi):
      maxi=l[i]
  return maxi

def list_appendbefore(l,z):
  newl=[]
  for i in range(len(z)):
    newl.append(z[i])
  for i in range(len(l)):
    newl.append(l[i])
  return newl

def list_appendend(l,z):
  newl=[]
  for i in range(len(l)):
    newl.append(l[i])
  for i in range(len(z)):
    newl.append(z[i])
  return newl

def list_average(l):
  sum=0
  for i in range(len(l)):
    sum=sum+l[i]
  ans=sum/len(l)
  return ans

l=[1,2,3,4,5,-10,6,4,100]
print(list_min(l)) #-10
print(list_max(l)) #100
z=[10,20,30]
print(list_appendbefore(l,z)) #[10, 20, 30, 1, 2, 3, 4, 5, -10, 6, 4, 100]
print(list_appendend(l,z)) #[1, 2, 3, 4, 5, -10, 6, 4, 100, 10, 20, 30]
print(list_average(l)) #12.777777777777779

#Types of Function Arguments

def add(a, b, c):
    return (a + b - c)

print(add( a = 20,b = 30,c =  40)) #10
print(add(20, 30, 40))

#next
def add(c, a = 20, b = 30):
    return (a + b - c)
print(add(40))  #10
print(add(40, 10)) #0
print(add(40, 10, 50)) #20

# Types of Functions

'''
#inbuilt functions
print(), input() ,len()

#library functions
math.log(), math.sqrt(), random.random() ,randrange(), round(), str(), sum(), type(), reversed(), range(), max(), min(), map(), filter(), zip(),

#string methods (functions)
''.upper(), "".lower(), title(), capitalize(), swapcase(), isupper(), islower(), isdigit(), isalpha(), index(), replase(), split()
'''
#user defined functions
def square(x):
 sqr = x ** 2
 return sqr  

print(square(5))














