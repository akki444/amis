from package.getparams import getParam
from package.editWord import editWord
try:
    lst1 = getParam()
    lst = lst1[0].split()
    lst1[1] = int(lst1[1]) 
    editWord(lst,lst1[1])
except:
    print("Неправильно введеные данные.")
    


