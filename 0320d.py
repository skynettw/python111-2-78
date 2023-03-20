import csv
with open("bodyinfo.csv", encoding='utf-8') as fp:
    datareader = csv.DictReader(fp)
    #heights = [int(d['height']) for d in datareader]
    data = [dict(d) for d in datareader]
print(data)
        