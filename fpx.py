from json import load
with open("rawData.json","r",encoding='utf-8') as file:
    data=load(file)
print(data.keys)