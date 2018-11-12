def editWord(lst,size,i=0):
    
    if(len(lst)==i):
        pass
    else:
        if(len(lst[i])==size):
            a = lst[i][0:len(lst[i])-1] + "  " + lst[i][len(lst[i])-1]
            print(a + " ",end='')
        else:
            print(lst[i] + " ",end='')
        i = i+1
        editWord(lst,size,i)
