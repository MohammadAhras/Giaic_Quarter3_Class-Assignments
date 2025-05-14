# control_flow_loops.py

#conditional statements
x= 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is Less than or equal to 10")

#Lopps
fruits = ["Apple", "Banana", "Cheery", "Grapes"]
for fruit in fruits:
    print(fruit) 

i= 0
while i < 5:
    print(i)
    i += 1

#Break and Continue statements
for i in range(5):
    if i ==3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)
