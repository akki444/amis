def getParam():
    text = input("Введите текст")
    size = input("Введите размер слов которые будут отредактированы:")
    if(text=="" or text==None or size == None):
        output = 1
        return output
    else:
        lst = []
        lst.append(text)
        lst.append(size)
        return lst
