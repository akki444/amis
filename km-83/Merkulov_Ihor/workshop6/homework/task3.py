def toUpper(str):
    list1 = str.split()
    str1 = ""
    for i in list1:
        str1 = str1 + i.title() + " "
    return str1



str1 = "red dead redemption"
print(toUpper(str1))