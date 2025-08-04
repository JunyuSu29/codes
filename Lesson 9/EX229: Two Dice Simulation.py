from random import randint
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
count11=0
for i in range(1001):
    a=randint(1,6)
    b=randint(1,6)
    total=a+b
    print(i)
    print(total)
    if total==2:
        count1+=1
    elif total==3:
        count2+=1
    elif total==4:
        count3+=1
    elif total==5:
        count4+=1
    elif total==6:
        count5+=1
    elif total==7:
        count6+=1
    elif total==8:
        count7+=1
    elif total==9:
        count8+=1
    elif total==10:
        count9+=1
    elif total==11:
        count10+=1
    else:
        count11+=1

percent1=round(float(100*(count1/1000)),2)
percent2=round(float(100*(count2/1000)),2)
percent3=round(float(100*(count3/1000)),2)
percent4=round(float(100*(count4/1000)),2)
percent5=round(float(100*(count5/1000)),2)
percent6=round(float(100*(count6/1000)),2)
percent7=round(float(100*(count7/1000)),2)
percent8=round(float(100*(count8/1000)),2)
percent9=round(float(100*(count8/1000)),2)
percent10=round(float(100*(count10/1000)),2)
percent11=round(float(100*(count11/1000)),2)

print("Here is the dictionary for the frequency percentage for each of the sums")
dict={2:f"{percent1}%",
      3:f"{percent2}%",
      4:f"{percent3}%",
      5:f"{percent4}%",
      6:f"{percent5}%",
      7:f"{percent6}%",
      8:f"{percent7}%",
      9:f"{percent8}%",
      10:f"{percent9}%",
      11:f"{percent10}%",
      12:f"{percent11}%"}
print(dict)
