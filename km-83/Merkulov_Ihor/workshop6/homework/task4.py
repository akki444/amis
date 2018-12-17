def addPoint(key,values,dataset):
    dataset[key] = values
    return dataset

data = {
    "Product":{"apple","orange","grape"},
    "Game":{"dmc","gta","callofduty"}
}
print(data)
addPoint("Anime",{"death note","mirai nikki","gintama"},data)
print(data)
