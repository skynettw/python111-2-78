f = open("bodyinfo.csv", "r", encoding="utf-8")
rawdata = f.readlines()
f.close()
for item in rawdata:
    name, h, w = item.split(",")
    print(name, round(int(w) / (int(h)/100)**2, 2))