dataset = {
    "Igor":17,
    "Johnny":18,
    "Dima":20,
    "Andrey":30,
    "Olya":6,
    "Hitler":129,
    "Egor":45
}
top = ""
age = 0
for i in dataset:
    if dataset[i]>age:
        top = i
        age = dataset[i]


dataset.pop(top)
print(top,age)
top =""
age = 0
for i in dataset:
    if dataset[i]>age:
        top = i
        age = dataset[i]
dataset.pop(top)
print(top,age)
top =""
age = 0
for i in dataset:
    if dataset[i]>age:
        top = i
        age = dataset[i]
dataset.pop(top)
print(top,age)