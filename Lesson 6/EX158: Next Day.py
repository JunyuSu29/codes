year=int(input("Enter a year"))
month=int(input("Enter a month (1-12)"))
day=int(input("Enter a day (1-31)"))
def leap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
if month in [1,3,5,7,8,10] and day in range(1,31):
    print(f"The next day is {year}-{month}-{day+1}")
elif month in [1,3,5,7,8,10] and day==31:
    print(f"The next day is {year}-{month+1}-1")
elif month in [4,6,9,11] and day in range(1,30):
    print(f"The next day is {year}-{month}-{day+1}")
elif month in [4,6,9,11] and day==30:
    print(f"The next day is {year}-{month+1}-1")
elif month==2 and leap(year)==True:
    if day in range(1,29):
        print(f"The next day is {year}-{month}-{day+1}")
    elif day==29:
        print(f"The next day is {year}-{month+1}-1")
elif month==2 and leap(year)==False:
    if day in range(1,28):
        print(f"The next day is {year}-{month}-{day+1}")
    elif day==28:
        print(f"The next day is {year}-{month+1}-1")
elif month==12 and day in range(1,31):
    print(f"The next day is {year}-{month}-{day+1}")
elif month==12 and day==31:
    print(f"The next day is {year+1}-1-1")
