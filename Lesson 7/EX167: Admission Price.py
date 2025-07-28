ages=input("Enter the age of one person of your group (type exit if you are done):")
total_price=0
while ages!="exit":
    age=int(ages)
    if age<0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age in range(3,13):
        total_price+=14
    elif age in range(13,65):
        total_price+=23
    elif age>=65:
        total_price+=18
    elif age in range(0,3):
        total_price+=0
    else:
        print("Invalid age input. Please enter a valid age.")
    ages=input("Enter the age of one person of your group (type exit if you are done):")
    
print(f"The total admission price for your group is ${total_price}.")
