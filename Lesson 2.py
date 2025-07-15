#By sep='' and end='', we can customize the seperators and endings of our output statement using print. For example:
print("CP club","sample","on","python","print","function",sep='  ^  ',end='  ')
#By using type() function, we can determine the type of a variable. For example:
print(type('3'))
#int() converts a data type to an integer. For example:
print(int("123"))
#Multiple-line comments: uses ' ' ' or " " " as a determiner. For example:
'''
    This is a multiple-line comment
    Just an example
'''



#CCC 23' J2
num=int(input())
SHU=0
for i in range(num):
    respond=str(input())
    if respond=="Poblano":
        SHU+=1500
    elif respond=="Mirasol":
        SHU+=6000
    elif respond=="Serrano":
        SHU+=15500
    elif respond=="Cayenne":
        SHU+=40000
    elif respond=="Thai":
        SHU+=75000
    elif respond=="Habanero":
        SHU+=125000
    
print(SHU)