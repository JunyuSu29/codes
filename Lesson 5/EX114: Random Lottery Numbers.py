import random
lottery_numbers=random.sample(range(1,50),6)
order=sorted(lottery_numbers)

print("Your lottery numbers are:",order)
