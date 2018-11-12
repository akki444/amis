from package.inputElement import inputElem
def minElem(lst,prelem,i=0):
    if(i==len(lst)):
        print(prelem)
    else:
        if(int(lst[i])< int(prelem)):
            prelem = lst[i]
        i = i + 1    
        minElem(lst,prelem,i)
try:        
    lst = []
    inputElem(lst)
    minElem(lst,lst[0])
except:
    print("Неправильно введеные данные.")

    
