def NZP(lst):
    N=[]
    Z=[]
    P=[]
    for i in lst:
        if i<0:
            N.append(i)
        elif i==0:
            Z.append(i)
        else:
            P.append(i)
    
    final_lst=N+Z+P
    return final_lst
print(NZP([-2,0,-4,9,0,3,1,-1]))