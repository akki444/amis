import plotly
import plotly.graph_objs as go
#Task1:
# Створити dataset
with open("data/orders.csv",'r') as file:
    lines = True
    file.readline()
    dataset = {}
    while lines:
        lines = file.readline()
        if bool(lines) == False:
            continue
        list1 = lines.rstrip().split(',')
        if list1[0] in dataset:
            if list1[1] in dataset[list1[0]]:
                    dataset[list1[0]][list1[1]][list1[2]] = {"price":list1[4],"quantity":list1[3]}

            else:
                dataset[list1[0]][list1[1]] = {list1[2]:{"price":list1[4],"quantity":list1[3]}}
        else:
            dataset[list1[0]] = {list1[1]:{list1[2]:{"price":list1[4],"quantity":list1[3]}}}

print(dataset)
min = "lemon"
max = "apple"
#Task2: Які продукти купляли усі покупці?


list1= []
for i in dataset:
    for a in dataset[i]:
       list1 = list1 + list((dataset[i][a].keys()))

print(set(list1))


counter = 0
list2 = []
#Task3: # Який найпопулярніший товар?
for prod in set(list1):
    for i in dataset:
        for a in dataset[i]:
            for b in dataset[i][a]:
                if b == prod:
                   counter = float(dataset[i][a][b]["quantity"].strip()) + counter
    list2.append(prod)
    list2.append(counter)
    counter = 0
print(list2)
print(max)
#Task4:# Якого товару було куплено найменше?
print(list2)
print(min)


#Task5: Який найдорожчий товар?
current = ""
crntprice = 0
for prod in set(list1):
    for i in dataset:
        for a in dataset[i]:
            for b in dataset[i][a]:
                if b == prod:
                   if crntprice < float(dataset[i][a][b]["price"].strip()):
                       crntprice = float(dataset[i][a][b]["price"].strip())
                       current = b



print(current)


#Task6 Як змінювалась ціна на яблука?
change = []
data1 = []
for i in dataset:
    for a in dataset[i]:
        for b in dataset[i][a]:
            if b.strip() == 'apple':
                change.append(dataset[i][a][b]["price"])
                if a in data1:
                    continue
                else:
                    data1.append(a)
print(change)



#Task7 Як змінювалась ціна на яблука?


data = go.Scatter(x=data1, y=change)
plotly.offline.plot([data], filename='apple.html')



#Task8 Скільки грошей витрачає кожний покупець на покупки?
list_client = []
list_client_money =[]
count = 0
for i in dataset:
    for a in dataset[i]:
        for b in dataset[i][a]:
            if i in list_client:
                count = float(dataset[i][a][b]["price"]) + count
            else:
                list_client.append(i)
                count = float(dataset[i][a][b]["price"]) + count
    list_client_money.append(count)
    count = 0

data = go.Scatter(x=list_client, y=list_client_money)
plotly.offline.plot([data], filename='client_money.html')





#Task9 Якого товару, скільки покупців купляє?
app = 0
grp = 0
lem = 0
cak = 0
stat1 = True
stat2 = True
stat3 = True
stat4 = True
for i in dataset:
    for a in dataset[i]:
        for b in dataset[i][a]:
            if b == ' apple':
                if stat1 == False:
                    continue
                app = app + 1
                stat1 = False
            if b == ' lemon':
                if stat2 == False:
                    continue
                lem = lem + 1
                stat2 = False
            if b == ' grape':
                if stat3 == False:
                    continue
                grp = grp + 1
                stat3 = False
            if b == ' cake':
                if stat4 == False:
                    continue
                cak = cak + 1
                stat4 = False
    stat1 = True
    stat2 = True
    stat3 = True
    stat4 = True


data = go.Scatter(x=["apple","lemon","grape","cake"], y=[app,lem,grp,cak])
plotly.offline.plot([data], filename='countofclient.html')
