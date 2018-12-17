def getList(lst1,i=0):
    if len(lst1)-1<3*i:
        pass
    else:
        print(lst1[3*i])
        i = i + 1
        getList(lst1,i)



lst1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
getList(lst1)