file = open("data/billboard_lyrics_1964-2015.csv")
info = file.read()
list1 = []
i= 0
while i != 3000:
    list1.append(info.splitlines()[i].split(","))
    print(i)
    i = i + 1
dataset = {

}
del list1[0]
for i1 in list1:
    dataset[i1[2]] = {i1[1]:{
        "Year": i1[3],
        "Rank": i1[0],
        "Lyrics": i1[4],
        "Source": i1[5]
    }}



print(dataset['"bon jovi"'])