listToSort=[4,5,78,3,7,-1,0,-6,-8,5,54,32]

def merge(list1,list2):
    final=[]
    while list1 and list2:
        if list1[0]>list2[0]:
            final.append(list2.pop(0))
        else:
            final.append(list1.pop(0))

    if not list1:
        for i in list2:
            final.append(i)

    if not list2:
        for j in list1:
            final.append(j)

    return final


def sort(finalList):
    if not finalList or len(finalList)==1:
        return finalList

    leftList=sort(finalList[:len(finalList)//2])
    rightList=sort(finalList[len(finalList)//2:])

    return merge(leftList,rightList)

newList=sort(listToSort)     
print(newList)

