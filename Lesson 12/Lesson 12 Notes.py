#WHen debugging, first look at the error message, and then start to print statements within loops if possible for further checking. 
contractor_hours = {}
contractor_hours['James'] = 10
contractor_hours['Purvi'] = 4
contractor_hours['Sherlin'] = 20
# print them sum of the weights of all pets
contractor_hours['total hours'] = sum(contractor_hours.values())
print(contractor_hours) #Type error: sum() function can't be used for just dictionaries, so we have to use .values() method to specify the sum of the values of the dictionary.

#Syntax Error: when the operator is unable to understand a line of code. This is the most basic type of error. 
#Logic Error: most difficult type of error to find, because they give unpredictable results. 
def Welcome_Message(name, id):
  print("Hello " + name + " and welcome to your "+ str(id) +" We know you will rock.")
print(Welcome_Message("Jack", 2022075))

def circle_area(r):
  PiConstantnumber = 3.1415926
  area = r * r * PiConstantnumber
  return area
print(circle_area(4))

def friends_time(num_hours, num_friends):
  print(f"You should spend {round(num_hours/num_friends,2)} hours with each of your friends on the weekend.")

friends_time(7,3)

def travel_time(minutes):
  if minutes > 60 and minutes<(24*60):
    print(f"You have {minutes//60} hours and {minutes%60} minutes left to reach your destination.")
  elif minutes > (60*24):
    print(f"You have {minutes//(60*24)} days, {(minutes-60*24)//(60*24)} hours and {minutes%(60)} minutes left to reach your destination.") 
  else:
    print(f"You have {minutes%60} minutes left to reach your destination.")
travel_time(2491)

def remove_nums(int_list):
  #list starts with 0 index that's why we will start from item at index 2
  for i in range(2,len(int_list),3):
    print(i)
    int_list.pop(i)
  return int_list
print(remove_nums([10,20,30,40,50,60,70,80,90]))