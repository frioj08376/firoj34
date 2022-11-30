# ax**2+b*x+c=0
'''
where a,b,c are real numbers.
a!=0
discriminants= (b**2)-(4*a*c)
'''

a=int(input("enter the value of a (a!=0) :"))
b=int(input("enter the value of b :"))
c=int(input("enter the value of c :"))

#discriminants.......

d=(b**2)-(4*a*c)

value1=((-b-(d)**0.5)/(2*a))
value2=((-b+(d)**0.5)/(2*a))
print("the roots are  :", value1,value2)


