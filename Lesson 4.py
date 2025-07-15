'''
Lists
A collection of positionally-ordered values of any type (you can even have multipl types in the same list!)
Mutable
Dynamically Resizable (They can be shortened or extended as needed)
'''
listo=["A","B",100]
first_id=id(listo)
print(first_id)

#Adding elements into list: use .append() function
listo.append(4)
print(listo)

#To create a list, either use an empty list [], or define a list with specific items 
#Nested lists: lists within lists
lst=["Bob",40.0,['dev','mgr']]
print(lst[2]) #Use [index position] to find an item in a list using positions

#Average calculator
def avg(list):
    return sum(list)//len(list)
print(avg([80,85]))

#Remove duplicates
def remove_duplicates(list1):
    unique=[]
    for item in list1:
        if item not in unique:
            unique.append(item)
    return unique
print(remove_duplicates([1,1,1,2,2,3,3,4,4,5,6,6]))

'''
Tuples
A tuple is an immutable sequence of arbitary objects that are also:
    -Fixed-length
    -Heterogeneous
    -Arbitrarily nestable
'''
#Empty tuple
tup=()

#A one-item tuple (not an expression)
tup=(0)
print(tup)

#A 4-item tuple
tup1=(0,'Ni',1.2,3)
print(type(tup1))

#Python allows you to assign values to multiple variables in one line, as tuples
x,y,z="Orange","Banana","Cherry"
print(f"the x fruit is {x}")
print(f"the y fruit is {y}")
print(f"the z fruit is {z}")

#Swapping values in tuples
a=5
b=6
a,b=b,a
print(a)
print(b)

#Storing grades
scores_and_names=[]
for i in range(3):
    line=input().split()
    name=line[0]
    score=int(line[1])
    scores_and_names.append((name,score))
    
top=scores_and_names[0]
for student in scores_and_names:
    if student[1]>top[1]:
        top=student
print(top[0])

#Swapping tuple values
for i in range(4):
    line=input().split()
    a,b=line[1],line[0]
    print((a,b))



