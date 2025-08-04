#Dictionaries: a collection of key value pairs with unique keys. 
#Use D[key] to access the value associated with the key. 
#Dictionaries are mutable, meaning you can change them after creation.
#Use .get(key,value) to access a value with a default if the key is not found. 
#To update a value that is tied to a key, use D[key]=new_value. 
#Use 'in' to check if a key (and not a value) is in the dictionary. 
D={'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(D['key1'])  # Output: value1
print(D.get('key4', 'default_value'))  # Output: default_value
D['key1']='value'
print(D)
print('key2' in D)  # Output: True

#Use the len() function to get the number of key-value pairs in a dictionary. 
#Use the .keys() and .values() methods to get all keys and values, respectively. Use list() on the outer to create a list of them. 
print(len(D)) # Output: 3
print(list(D.keys()))  # Output: ['key1', 'key2', 'key3']
print(list(D.values()))  # Output: ['value', 'value2', 'value3]

#Use .update() method to add or update multiple key-value pairs at once. 
D.update({"key4":"value4", "key5":"value5"})
print(D)
#Use .pop(key) to remove a key-value pair and return the value.
D.pop('key2')
print(D)
#Use .items method to return the key-value pair entries.
items=D.items()
print(items)

#A set is a collection of unordered, unique, and immutable values. 
colors={'red','black','white','blue','blue'} 
print(colors) #Remove duplicates. 

#Use A|B or A.union(B) to generate a set that contains all items in set A OR set B
A={1,2,3,4,5}
B={1,3,5,7,8}
union=A.union(B)
print(union)

#A&B or A.intersection(B) to generate a set that contains all items in set A AND set B
intersection=A.intersection(B)
print(intersection)

#Aliasing function: assign a variable to a function 

