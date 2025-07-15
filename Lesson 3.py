#Lesson 3: Strings
#Strings are immutable sequences, positionally ordered collections of other objects that cannot be modified. 
#Triple quote is able to print multiple lines of strings. For example:
str='''Here is a list of names all on different lines
Bob
Sally
Joe
Karen'''
print(str)

#"\" is the escape character for python. 
#\n is used for having a newline.
#\t is used for tab
print("Bob\tSally\nJoe") #Tab (Whole space) after Bob, and then print Sally, then the start of next line print Joe.

#Raw string: the computer interprets the whole string as normal; ignores the manipulations like \n \t. For example:
raw_string=r"C\D\E\n"
print(raw_string)

#String Formatting: use {} to make the positions of the strings, and then use .format() function to insert the strings into the positions
f_str="Address={} {} {}".format("888","Cobler","Road") #Add space in between {}'s to make the actual string have the wanted spaces.  
print(f_str)

#By absolute position, {index}, where index is an integer. Starts with 0, goes from left to right. 
f_str2="Hello {2} {0} and Bye {1}".format("Enoch","Chris","Luke") #The integers represent the sequence of the strings in the format function. For example, the {2} would be replaced by the string that is the 3rd position inside the format bracket (Since it starts with 0).
print(f_str2)

#We can also use the format function by keyword. 
f_str3="{number} {action} for a bird, one giant leap for {beneficiaries}!"\
    .format(number=1,action="small flap",beneficiaries="bird kind")
print(f_str3)

#Formatted string literals. Uses f'' function
num=888
name="Cobbler"
suffix="Rd."
f_str4=f"Address={num} {name} {suffix}"
print(f_str4) #Instead of formatting after making the positions, this functionuses variables to assign to strings, and then use {} to assign the positions of the variables (That is, the assigned strings).

#Area of a Field
length=int(input("Enter the length of the field in feet"))
width=int(input("Enter the width of the field in feet"))
area_in_acre=(length*width)/43560
final_area=round(area_in_acre,2)
print(f"The area of the field in acre is {final_area} acres")

#Tax and Tip
original_cost=int(input("Enter the cost of the order before tax and tip."))
tax=float(original_cost*0.13)
tip=float(original_cost*0.18)
final_cost=round(original_cost+tax+tip,2)
print(f"The final cost of the order with tax and tip is ${final_cost}.")