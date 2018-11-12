from package.inputElement import inputElem

def printList(lst,i=0):
    if(len(lst)==i):
        pass
    else:
        print(lst[i])
        i = i +1 
        printList(lst,i)    

try:
    lst = []
    inputElem(lst)
    lst.reverse()
    printList(lst)
except:
    print("Неправильно введеные данные.")
