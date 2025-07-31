import random
import string

def generate_license_plate():
    letters=0
    digits=0
    plate=''
    letters_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    type=random.choice(['old','new'])
    
    if type=='old':
        
        while letters<3:
            plate+=random.choice(letters_list)
            letters+=1
        
        while digits<3:
            plate+=str(random.randint(0,9))
            digits+=1


    else:
        
        while digits<4:
            plate+=str(random.randint(0,9))
            digits+=1
        
        while letters<3:
            plate+=random.choice(letters_list)
            letters+=1
    
    return plate
my_plate=generate_license_plate()
print(f"Your random license plate is: {my_plate}")
