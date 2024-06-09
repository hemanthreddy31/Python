#string input
name=input("enter your name")
print(name)
print(type(name))

#integer input
numberone=int(input("enter the numberone"))
print(numberone)
print(type(numberone))

#multiple inputs
data=input("enter information").split()
name=data[0]
age=data[1]
profession=data[2]

print(data)
print(name)
print(age)
print(profession)