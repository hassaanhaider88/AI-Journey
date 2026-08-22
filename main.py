a = [1,3,5,21,34,2,2,6,64,4,23,22,2,2,2,24,4,4]

b = []
c = []

for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

print("even number:",b) 
print("Odd number:",c) 