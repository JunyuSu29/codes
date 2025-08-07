def avg(nums):
    avg=float(sum(nums)/len(nums))
    below=[]
    at=[]
    above=[]
    for num in set(nums):
        if num<avg:
            below.append(num)
        elif num==avg:
            at.append(num)
        else:
            above.append(num)
    
    return f"The average of the list of numbers is {avg}, the numbers below average are: {below}, the numbers above average are: {above} "
print(avg([2,2.5,3,3.5,4,4.5,5]))

 