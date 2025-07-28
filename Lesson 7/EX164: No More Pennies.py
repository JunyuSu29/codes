price=input("Enter the price:")

total=0.0
while price!="exit":
    total+=float(price)
    price=input("Enter the price:")

print(f"The total price is: {total}")

remainder=(total*100)%5
if remainder<2.5:
    total-=(remainder/100)
else:
    total+=(5-remainder)/100
print(f"The total price rounded to the nearest nickel is {total}")