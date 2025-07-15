#Making Change
num_of_cents=int(input("Enter the number of cents"))
value=float(num_of_cents*0.01)
penny=0.01
nickel=0.05
dime=0.1
quarter=0.25
loonie=1
toonie=2
toonies=int(value//toonie)
value-=toonies*toonie
loonies=int(value//loonie)
value-=loonies
quarters=int(value//quarter)
value-=float(quarters*0.25)
dimes=int(value//dime)
value-=float(dimes*dime)
nickels=int(value//nickel)
value-=float(nickels*nickel)
pennies=int(value//penny)
value-=float(pennies*penny)
output=f"The change is: \n{toonies} toonie/toonies\n{loonies} lonnie/loonies\n{quarters} quarter(s)\n{dimes} dime(s)\n{nickels} nickel(s)\n{pennies} penny/pennies."
print(output)

#Day old bread
loaves=int(input("How many loaves did you purchase?"))
original_price=round(float(loaves*3.49),2)
discount=round(float(loaves*0.6),2)
final_price=round(float(original_price-discount),2)
print(f"You purchased {loaves} loaves")
print(f"The original price is ${original_price}")
print(f"Since they are all day old breads, you get ${discount} discount")
print(f"So the final price is ${final_price}")