#Default in a function: when we don't pass an argument, it uses the already assigned value. 
#For example: 
def greet(name="World"):
    return f"Hello, {name}!"
print(greet()) #Output: Hello, World!
print(greet("Johnny")) #Output: Hello, Johnny!

#Collecting Kewword Arguments: using ** kwargs to collect keyword arguments into a dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Johnny", age=25, city="New York")

#Unpacking Arguments: using *args to unpack a list or tuple into individual arguments
def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3)) #Output: 6

