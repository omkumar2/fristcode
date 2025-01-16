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









