# swaping two numbers without third variable

a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
print("print the values before swaping...")
print(a)
print(b)

a=a+b
b=a-b
a=a-b
print("print values after swaping....")
print(a)
print(b)