def remove_duplicate(List):
    newlist = []
    for num in List:
            if num not in newlist:
                newlist.append(num)
    return newlist

List = [3,3,3,3,1,3,2,6,7,10,10,22,22,1,1,10,2,3,2,2,1,1,1,4,5] 
print(remove_duplicate(List))
