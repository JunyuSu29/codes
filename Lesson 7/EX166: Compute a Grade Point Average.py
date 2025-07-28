letter_to_grade={"A+": 4.0, 
"A": 4.0,
"A-": 3.7,
"B+": 3.3,
"B": 3.0,
"B-": 2.7,
"C+": 2.3,
"C": 2.0,
"C-": 1.7,
"D+": 1.3,
"D": 1.0,
"D-": 0.7,
"F": 0.0}
grades=input("Enter a letter grade uppercased")
total=0.0
count=0
while grades!="exit":
    total+=letter_to_grade[grades]
    count+=1
    grades=input("Enter a letter grade uppercased")

average=(total/float(count))
print(f"The average of all the grade points you submitted is {average:.2f}")

