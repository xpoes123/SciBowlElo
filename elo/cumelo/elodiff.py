elos = []
teams = []
teamsElo = []
teamsDict = {}

mset = set()
with open("/Users/davidjiang/cs/fun/elo/cumelo/readme.txt") as f:
    index = 0
    for line in f:
        if line[0] == "~":
            continue
        nl = line[:-1].split("\t")
        nl[0] = nl[0].upper()
        mset.add(nl[0])
    for line in mset:
        add = []
        name = line.rstrip('\n')
        teams.append([name, 0])
        teamsElo.append([name, 0])
        teamsDict[name] = index
        index += 1
    

l = 684
r = 821
d = 10
with open('/Users/davidjiang/cs/fun/elo/cumelo/cumelooutput.txt', 'w') as p:
    with open("/Users/davidjiang/cs/fun/elo/cumelo/readme.txt") as f:
        for line in f:
            if line[0] == "~":
                elos.append(-1)
                continue
            nl = line[:-1].split("\t")
            nl[0] = nl[0].upper()
            elos.append(nl)
        match = 0
        inbetween = []
        for i in elos:
            if i == -1:
                match += 1
                for j in teams:
                    j.append(teamsElo[teamsDict.get(j[0])][1])
                for k in inbetween:
                    teams[teamsDict.get(k[0])][match+1] = k[1]
                    teamsElo[teamsDict.get(k[0])][1] = k[1]

                inbetween = []
                continue
            inbetween.append(i)


sortedElo = []

for i in teams:
    if abs(float(i[r-1]) - float(i[l-1])) > 0.1:
        add = []
        if float(i[l-1]) < 1:
            add.append(i[0])
            add.append(round(float(i[r-1]) - float(1200),4))
        else:
            add.append(i[0])
            add.append(round(float(i[r-1]) - float(i[l-1]),4))
        sortedElo.append(add)
            
# print(sortedElo)
sortedElo  = sorted(sortedElo, key = lambda x:x[1], reverse = True)
# print(sortedElo)
for i in sortedElo:
    print(i[0], i[1])
