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