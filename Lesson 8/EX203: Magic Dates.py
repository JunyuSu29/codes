def isMagic(day,month,year):
    year=str(year)
    year=year[2:]
    if day*month==int(year):
        return True
    return False

thirtymonths=[4,6,9,11]
thirty_one_months=[1,3,5,7,8,10,12]
result=[]
for year in range(1900,2000):
    for month in range(1,13):
        if month in thirtymonths:
            for day in range(1,31):
                if isMagic(day,month,year):
                    result.append(f"{day}-{month}-{year}")
        
        elif month in thirty_one_months:
            for day in range(1,32):
                if isMagic(day,month,year):
                    result.append(f"{day}-{month}-{year}")
        else:
            for day in range(1,29):
                if isMagic(day,month,year):
                    result.append(f"{day}-{month}-{year}")
print("Magic Dates during the 20th century are:")
print(result)
                    
