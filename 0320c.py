f = open("bodyinfo.csv", "r", encoding="utf-8")
rawdata = f.readlines()
f.close()

data = [item.split(",") for item in rawdata[1:]]
heights = [int(d[1]) for d in data]
weights = [int(d[2]) for d in data]
bmis = [round(int(d[2]) / (int(d[1])/100)**2,2) for d in data]
'''
bmis = list()
for d in data:
    w = int(d[2])
    h = int(d[1])
    bmi = w / (h/100)**2
    bmis.append(round(bmi, 2))
'''
print(bmis)
print("本班最高的學生是{}公分".format(max(heights)))
print("本班最矮的學生是{}公分".format(min(heights)))
print("本班平均身高是{}公分".format(round(sum(heights)/len(heights)),2))
'''
names = list()
heights = list()
weights = list()
for item in rawdata:
    name, height, weight = item.split(",")
    names.append(name)
    heights.append(height)
    weights.append(weight)
'''
#print(names)
#print(heights)
#print(weights)