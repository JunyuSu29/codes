def tokenizer(s):
    numbers=['0','1','2','3','4','5','6','7','8','9']
    operators=['+','-','*','/','%','(',')','[',']','{','}','^','=']
    tokens=[]
    empty_string=''
    digit_counter=0

    for token in s:
        while token in numbers:
            digit_counter+=1
        if digit_counter>1:
            


