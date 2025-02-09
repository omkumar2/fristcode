
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








