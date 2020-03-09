"""

for i in range(1,101):
    print(i)

l=[]
for i in range(1,101):
   l.append(i)

l=[i for i in range(1,101)]
"""

TableNumber=int(input("Enter Table Number : "))
l=[]
for i in range(1,13):
   l.append(i*TableNumber)
#l=[i*TableNumber for i in range(1,13)]

print(l)