def removeOutliers(lst):
    if len(lst)<4:
        return "Error! This program only works when your list has 4 or more items contained!"
    sorted_list=sorted(lst)
    return sorted_list[2:-2]

print(removeOutliers([0,200]))
print(removeOutliers([2,4,5,3,1,7,6,8,9]))