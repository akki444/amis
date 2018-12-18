import re
import plotly as pl
import plotly.graph_objs as go

def getDataset(rank,song,artist,year,dataset):
    if artist in dataset:
        if year in dataset[artist]:
            dataset[artist][str(year)][song] = rank
        else:
            dataset[artist][str(year)] = {song:rank}
    else:
        dataset[artist] = {str(year):{
            song:rank
        }}
    return dataset

def getRank(line):
    list1 = re.split(r',',line,maxsplit=1)
    print("Rank:",list1[0])
    return list1[0],list1[1]

def getSong(line):
    list1 = re.split(r',',line,maxsplit=1)
    print("Song:",list1[0])
    return list1[0],list1[1]

def getArtist(line):
    list1 = re.split(r',',line,maxsplit=1)
    print("Artist:",list1[0])
    return list1[0],list1[1]

def getYear(line):
    list1 = re.split(r',',line,maxsplit=1)
    str1 = re.findall(r'\d\d\d\d',list1[0])
    print("Year:",str1[0])
    return str1[0],list1[1]


def drawGrap1(dataset):
    dataset_1 = {}
    for artist in dataset:
        for year in dataset[artist]:
            if bool(year in dataset_1)==False:
                dataset_1[year] = 0
            dataset_1[year] = len(dataset[artist][year]) + dataset_1[year]
    print(dataset_1)
    print(dataset_1.keys())
    print(dataset_1.values())
    data = go.Scatter(x = list(dataset_1.keys()), y = list(dataset_1.values()))
    pl.offline.plot([data], filename='grap1.html')

def drawGrap2(dataset):
    dataset_2 = {}
    for artist in dataset:
        if bool(artist in dataset_2) == False:
            dataset_2[artist] = 0
        for year in dataset[artist]:
            dataset_2[artist] = len(dataset[artist][year]) + dataset_2[artist]
    data = go.Pie(labels=list(dataset_2.keys()), values=list(dataset_2.values()))
    pl.offline.plot([data], filename='grap2.html')

def drawGrap3(dataset):
    dataset_3 = {}
    for artist in dataset:
        if bool(artist in dataset_3) == False:
            dataset_3[artist] = 0
        for year in dataset[artist]:
            dataset_3[artist] = len(dataset[artist][year]) + dataset_3[artist]
    data = go.Bar(x=list(dataset_3.keys()), y=list(dataset_3.values()))
    pl.offline.plot([data], filename='grap3.html')

def getCol(path):
    with open(path,mode='r') as file:
        dataset = {}
        file.readline()
        for line in file:
            if not line.rstrip():
                continue
            current_rank,line = getRank(line)
            current_song,line = getSong(line)
            current_artist,line = getArtist(line)
            current_year,line = getYear(line)
            getDataset(current_rank,current_song,current_artist,current_year,dataset)
             #  list1 = line.rstrip().split(',')
               # dataset = dict(zip(header,list1))
               # print(dataset[col_name])
        drawGrap1(dataset)
        drawGrap2(dataset)
        drawGrap3(dataset)

try:
    getCol("data/billboard_song.csv")
except ValueError as v_error:
    print("valueerror")
except IOError as io_error:
    print("ioerror")