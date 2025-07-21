'''
Python is a whitestaged language
C++, Java, JavaScript use braces {} to define blocks of code
But python uses indentation to define blocks of code, which makes it "whitespaced".
'''
#If statements: allows actions under a specific condition. 
#Else: if the if condition's boolean value is false, the actions under else will be performed.
#Elif: if the first if condition shows false, it checks the elif condition, otherwise it would skip to next elif or else. 
# Lines below the if/elif/else statements must be indented. 
#For example:
x=int(input("Enter a number: "))
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")

#For loops: a looping statement that steps through items in any sequence or an iterable object. 
#For examples, this code checks each item in a list through different conditions:
lst=[1,2,3,4,5]
for i in lst:
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")

#For i in range() function: if there is no comma in the range() function, it will start from 0 and end at the number before the given number. 
#For example, range(5) will return 0, 1, 2, 3, 4, or it would repeat an action 5 times. 
for i in range(5):
    print("This is iteration number", i)

#Enumerate() function: it is used to loop through a list and get the index of each item in the list. 
bird_weights= [1.2, 1.5, 0.8, 2.0]
for index, weight in enumerate(bird_weights):
    print(f"Bird #{index+1} weighs {weight} kg")

#While loops: a looping statement that continues performing an action as long as the condition's boolean value is true. 
x=5
while x>0:
    x-=1
    print("x is still positive")
    
raining=True
#raining=0
if raining: #If raining==True
    print("Don't forget an umbrella!")
else:
    print("Enjoy the nice weather!")

#Nested conditionals: if statements inside another if statement. 

raining=True
temperature=55
time="night"
#Option A
if time=="night":
    if raining:
        if temperature<60:
            print("It's a cold, wet evening.")

#Option B
if time=="night" and raining and temperature<60:
    print("It's a cold, wet evening.")

#And: a conditional statement with an and returns true if and only if both conditions are true. 
#In: a conditional statement checks if a value is in a sequence. 
