def inputElem(lst):
    elem = input("Введите число(если хотите остановиться напишите stop)")
    if(elem=="stop"):
        return lst
    else:
        lst.append(elem)
        inputElem(lst)
