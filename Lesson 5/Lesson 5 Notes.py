#Sequence Operations
#All sequence types support a series of useful operations
#Length function len() determines the size of a sequence value, and the result is an integer. 
print(len("Hello World"))

#Concatenation(+): combine sequence values together, and the result is a new sequence value.
#Example for string:
str1="hello"+"world"+"helloworld"
print(str1)

#Example for list:
lst=['a']
new_lst=lst+[4,5,6]
print(new_lst)

#Example for tuple: 
print((1,2)+(3,4))

#Concatentaiton is only supported when both sequences are of the same type, otherwise it would print error. 
'''
a=[1,2]+(3,4)
print(a)
'''

#Repetition(*): repeat a sequence value a certain number of times, and the result is a. new sequence value. 
#Example for string:
t='hi'*4
print(t)

#Example for lists:
new_lst=lst*2
print(new_lst)

#Example for tuples:
tup=(1,2)
new_tup=tup*4
print(new_tup)

#Containement(in): determines whether a sequence value is inside another one, and the result is a boolean value.
#Example for string:
print("M" in "MPCS") #True
print("T" in "MPCS") #False
print("CS" in "CS") #True

#Example for list:
print(4 in lst) #False
print('a' in lst) #True

#Example for tuples:
tup=(1,2,True,False,"Hi")
print("Bob" in tup) #False
print("2" in tup) #False because 2 is an integer in this specific tuple, not a string
print(1 in tup) #True

#Sequence indexing S[i]: fetches a single item from a sequence value.
#Example for string:
str1="spam" 
print(str1[0])

#Example for lists:
lst=['a','b',1]
print(lst[0])

#Example for tuples:
tup=(1,2,True,False,"Hi")
print(tup[3])

#Python also allows negative indexing, which starts from the end of the sequence.
#Example for string:
print(str1[-1]) #Last item
print(str1[-2]) #Second last item

#Example for lists:
lst=["Bob",['a','b','c'],5,6]
print(lst[-1])
print(lst[-3])

#Example for tuples:
tup=(1,2,True,False,"Hi")
print(tup[-1])
print(tup[-2])
#Sequence Slicing S[i:j], which returns an entire section of a sequence value. 
#The lower bound i is inclusive, whereas the upper bound j is exclusive
#For example:
S='MPSC51042'
lst=['Bob','Sally','Tina']
tup=(1,2,3,4,5)
print(S[0:4]) #From the 1st item to 4th item, but excludes the 4th item in terms of python counting which is 5th item. 
print(lst[1:3]) #From the 2nd to 3rd item but excluess the 3rd item, which is the 4th item in terms of python counting
print(tup[1:4]) #From the 2nd to 4th item, but excludes the 4th item, which is the 5th item in terms of python counting

#It can also be used as S[i:], which means the i-th item to the end of the sequence.
print(S[1:]) #From the 2nd item to the end
print(lst[1:]) #From the 2nd to the end
print(tup[2:]) #From the 3rd to the end

#It can also be used as S[:j], which means the start of the sequence to the j-th item, but excludes the jth position.
print(S[:3]) #From the 0th item to the 3rd item
print(lst[:-1]) #From the 0th item to the 2nd item, but excludes the last one -1
print(tup[:-2]) #From the 0th item to the 3rd (-last) item, but excludes the last two

#[:] simply creates a copy of the original sequence value.
print(S[:])
print(lst[:])
print(tup[:])

'''
String methods:
Python provides collection of methods that create new strings based on the bahaviour of the original string.
upper(): capitalizes all letters of the string
lopwer(): makes all letters of the string lowercase
split(): splits the string into a list of strings based on a specified seperator
find(): finds the first occurance of a specific item in the string and returns the index position
replace(): replace all occurances of a substring with a new substring.
strip(): returns a copy of the string with the leading and trailing removed.
'''
#range() function: creates a collection of integers from a starting point to an ending point, with an optional step value
r=range(4,17,2) #From 4 to 17, skip count by 2
print(r[0])
print(r[1])
print(len(r))
print(r)