plate=input("Enter a license plate:")
if len(plate)==6 and plate[0:3].isalpha() and plate[3:6].isdigit():
    print("The plate you submitted is valid for the older style.")
elif len(plate)==7 and plate[0:4].isalpha() and plate[4:7].isdigit():
    print("The plate you submitted is valid for the newer style.")
else:
    print("The plate you submitted is invalid in the province of Ontario.")
