f = open("data.txt", "r", encoding="utf-8")
data = f.readlines()
f.close()

scores = list()
for d in data:
    scores.append(int(d))
print("Max:", max(scores))
print("Min:", min(scores))
print("Average:", round(sum(scores)/len(scores), 2))

['50\n', '65\n', '54\n', '85\n', '96\n', '52\n', '31\n', '52\n', '68\n', '95\n', '41\n', '55\n', '85\n', '97\n'] 
[50, 65, 54, 85, 96, 52, 31, 52, 68, 95, 41, 55, 85, 97]