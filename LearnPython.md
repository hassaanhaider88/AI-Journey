print(f"Hello, {name}! Welcome to the program.") this is like literals in js where you can embbed any variable into console value

 print("he low")
 name = input("What is your name? ")

  Comments goes here
 print(f"Hello, {name}! Welcome to the program.")

 """
 Long comments goes here
 multiple lines
 """

## Numbers
 -> Natural
 -> Wohle
 -> Float
 -> Integers

## Imagenry Value
 a = 12 + 3j  j represent imagenry value
 print(type(a)) complex data type
 print(type(34))
 print(type(-34))
 print(type(3/4))

## Strings
 using "" or '' qoutes

## Boolean
 True or False 

 a = 0
 b = 1

 if a : 
     print("yes")
 else :
     print("Not")
## Unicode
 print(ord("a"))
 print(ord("A"))
 print(ord("🤣"))

 a = "SANNAY"
 print(a[0])
 print(a[1])
 print(a[2])
 print(a[-2]) start from last


## Slicing a[start: stop : step]
slicing have defauld values like start has 0 stop has (-1 or a.lenght - 1) and step has 1
 a = "SANNAY KHAN"
 print(a[0:-1 : 2])

 Type Conversion
 int(),float(),str(), bool() 

 import winshell

 try:
      Empties the bin silently without prompts, progress bars, or sounds
     winshell.recycle_bin().empty(confirm=False, sound=False)
     print("Recycle Bin permanently cleared!")
 except Exception as e:
      Handles cases where the bin is already empty
     print("Recycle Bin is already empty or couldn't be cleared.",e)


 + - * / // ** %
 print(23+23)
 print(23-23)
 print(23*23)
 print(23/23)
 print(23%23) Reminder
 print(23**2)  23 ki power 2 
 print(23//2)  float division never show . in output

"""
()
**
*  / // %
+ - 
"""

 print(23 == 23)
 print("23" == 23)

age = int(input("Please enter your age: "))

if type(age) != int or age < 0:
    print("Invalid input. Please enter a valid age.")

if age < 18:
    print("You are a minor.")
else :
    print("You are an adult.")

    rupe = input("enter the mount you have: ")

if rupe == "10":
    print("You have buy 10  cheez")
elif rupe == "20":
    print("You have buy 20 cheez")
elif rupe == "30":
    print("You have buy 30 cheez")
else: 
    print("You have not buy any cheez")




print(23 == 23.0)

# Range( start : stop : step )  # 

for n in range(10, 101, 1):
    print(n)
print("End of first loop")

for n in range(23, 57, 1):
    print(n)
print("End of second loop")

for n in range(45): # mean start from 0 and tell 45 with step of 1
    print(n)

for n in range(120, 100, -2):
    print(n)


for n in " Hassaan ":
    print(n)


a = "student"

for i in range(0,len(a),1):
    print(a[i])

    for n in range(120, 100, -2):
    if n == 110:
        break   => pore loop ko khatam krdo 
    print(n)

    for n in range(120, 100, -2):
    if n == 110:
        continue  => current step ko skip kro
    print(n)

    n = 5
for i in range(0,11, 1):
    print(f"{i} x {n} = {i*n}")

    a = 456
while a > 0:
    print(a % 10)
    a //= 10

    a = int(input("Ente a number : _"))
revers = 0
while a > 0:
    revers = (revers * 10) + (a % 10)
    a = a // 10
print(revers)
print(type(revers))

a = int(input("Ente a number : -"))
old = a
revers = 0
while a > 0:
    revers = (revers * 10) + (a % 10)
    a = a // 10
print(revers == old)

def MyFunc(n):
    if n <= 0:
        return
    print("Hello welcome to the HMK Emperor",n)
    MyFunc(n-1)


MyFunc(40)

def myFun(a,b):
  print(f"the value of a is {a} and b is {b}")
myFun(b=34,a=2)

order
list = ['has', 'been', 'updated', 'successfully']

print(list[1:3])

mutable
list = ['has', 'been', 'updated', 'successfully']

list[3] = "Hassaan"
list.append("HAIDER")
list.insert(1,"HAI HAI")

print(list)
duplicate
t = [4,2,3,3,3,4,21,3,5]

list = [3, -1, 4, -5, 9]
positive = []
negative = []
for i in list:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)

        
print("Positive numbers:", positive)
print("Negative numbers:", negative)

list = [10, 20, 30, 40]
total = 0

for num in list:
    total += num

print("the avg is ", total / len(list))

list = [4, 8, 2, 9,12, 1]
greatest = list[0]

for i in list:
    if greatest > i:
        continue
    else:
        greatest = i

print(greatest)

list = [4, 8, 2, 9,12, 1]
greatest = list[0]

for i in list:
    if greatest > i:
        continue
    else:
        greatest = i

list.remove(greatest)

secGreat = list[0]
for i in list:
    if secGreat > i:
        continue
    else:
        secGreat = i

print(secGreat)

s1 = {10,20,30,40} # Set
s2 = {30,40,50,60}

print(s1.difference(s2)) elements of s1 that are not present in s2
print(s2.difference(s1))  elements if s2 that are not present in s1
s2 -= s1
print(s2) this will update whole set (second wala)
print(s1.intersection(s2)) common elements in both sets

s2 & s1
s2 &= s1 this will update the orignel left sideed set
 


# ## Dictionary
# ##Create
# d = { "name": "Hassaan", "age": 25, "city": "Karachi" }

# ## Accessing Items
# print(d["name"])  ## Output: Hassaan

# ##Update
# d["name"] = "Ali"  ## Updating value
# print(d["name"])  ## Output: Ali

# ##Add
# d["address"] = "Pakistan"  ## Adding new key-value pair
# print(d)  ## Output: {'name': 'Ali', 'age': 25, 'city': 'Karachi', 'address': 'Pakistan'}

# ##Delete
# d.pop("age")  ## Removing key-value pair
# print(d)  ## Output: {'name': 'Ali', 'city': 'Karachi', 'address': 'Pakistan'}

d = { "name": "Hassaan", "age": 25, "city": "Karachi" }

# print(d.get("name")) # Hassaan
# print(len(d)) # 3
# print(d.keys()) # dict_keys(['name', 'age', 'city'])
# print(d.values()) # dict_values(['Hassaan', 25, 'Karachi'])
# print(d.items()) # dict_items([('name', 'Hassaan'), ('age', 25), ('city', 'Karachi')])
# print(d.popitem()) # ('city', 'Karachi') # this will remove the last inserted item from the dictionary
print(d.setdefault("age", 19)) # 25 # this will add the key-value pair if the key does not exist, otherwise it will return the value of the key
d.update({"age": 20, "country": "Pakistan"}) # None # this will update the value of the key if it exists, otherwise it will add the key-value pair

print(d)

# d = { "name": "Hassaan", "age": 25, "city": "Karachi" }
# # Travesing (Loops)

# for i in d:
#     print(d[i])  # This will print the values of the dictionary
#     print(i)  # This will print the keys of the dictionary

# d1 = { "name": "Hassaan", "age": 25, "city": "Karachi" }
# d2 = { "adress" : "Lahore pakistan", "age": 20, }

# # d1.update(d2)  # This will update the values of d1 with the values of d2
# # print(d1)  

# for i in d2: 
#     d1[i] = d2[i] 

# print(d1)  

# d = {"a" : 10, "b" : 20, "c" : 30, "d" : 40}

# sum = 0

# for n in d:
#     sum += d[n]

# print(sum)     

## counting frequency of characters in a string
# d = ["hello","hello","hello", "world", "hello", "python", "world", "hello","python"]

# # dic = {}
# # for i in d:
# #     if i in dic.keys():
# #         dic[i] = dic[i] + 1
# #     else:
# #         dic[i] = 1

# # print(dic)

# dic = {}

# for i in d:
#     if i in dic.keys():
#         dic[i] = dic[i] + 1
#     else :
#         dic[i] = 1


# print(dic)       

d1 = {"a": 10, "b" : 20,"c" :30}
d2 = {"c": 40, "d" :50,"e" :60}

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else :
       d1[i] = d2[i]


print(d1)
print("x" in d1.keys())


Exception Handling
# a = 10
# b = 0

# # print(a/b) ## ZeroDivisionError

# a = "19"
# b = 10
# # print(a + b) ## TypeError
# # let handle this error


# num = int("2asdf")
# print(num) ## ValueError
a = int(input("enter your 1st number: -"))
b = int(input("enter your 2nd number: -"))
try:
   print(a / b)
except Exception as err:
   print(f"Sorry an error is {err}")
else:
   print("not error occure ")
finally:
   print("if error or not error this will run every time")

name = input("Please enter your name._")
print(f"Thanks for makingn account {name}")

for rasing custom error messages
age = int(input("enter your age:-"));

if age < 18:
    raise TypeError("Your are not eligigle")

print("You are elegible")


# CRUD Files via python

# open("hello.txt","x") # create file

# file = open("hello.txt","r") # write file if not exist then add one"
# data = input("What you want to add: ")

# file.write(data)


# fileData = open("hello.txt",'r' );
# print(fileData.read())

with open("hello.txt","a") as fs:
    data = input("/n enter you data")
    fs.write(data)



# OOPS in Python
What is special about OOPS?
- Make your code more reuseable
- Easier to work with large Programs
- OOP programs prevent you from repeating code.
- OOP provide you security

## Class
-> A class is a blueprint for creating objects. 
Objects are instances of classes.
-> Syntax
class (keyword) className:
    property : values

varibales defind in class called attributes
functions defind in class called motheds

class Animsl:
   spcies = "Dog" # Arrtibute

   def maek_sound(self): # method
       print("bark!)

Accessing attributes and methods
class Car:
    a = 12

    def hello():
      return "hello AI ML"

### now hello1 become object
hello1 = Car
print(hello1.a)
print(hello1.hello())


## Constructors
https://youtu.be/IhG3UJzkjnw?list=PLiJFOrVU2fnFRbfj5vwG6AEZJrN0SAIiE&t=1597

## Encapsulations
=> Inprogarmming, Encapsulation si about keeping some info (data) safe adn only letting it be changed or looked at in specific work.
## Polymorphizm
=> mean heaving many forms.
matbl ke eak he cheez diffrent tasks perform kr paa rahi hai.
## Inheritance
=> When one class inherits (get) some features from another class this phenomena is known as inheritance
## Abstaction
=> when we see the seentail part of our code and hides the rest is the process of Abstaction.