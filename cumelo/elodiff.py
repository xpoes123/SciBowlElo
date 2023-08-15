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
    
CCWT = (2, 25)
SBST = (26, 143)
MIT2021 = (144, 245)
SBL = (246, 432)
LOST = (433, 542)
SBST2 = (543, 612)
DAST = (613, 658)
ASS = (659, 683)
MIT2022 = (684, 821)
CAST2022 = (822,871)
DASONI2022 = (872, 937)
PROMETHEUS2022 = (937, 1209)
ESBOT2022 = (1210, 1265)
NATS2022 = (1266, 1307)
MIT2023 = (1308, 1375)
NFSBL = (1376, 1507)
IGNIS2023 = (1508, 1912)
ESBOT2023 = (1913, 2012)
OLYMPUS2023 = (2013, 2155)
DASONI2023 = (2156, 2214)
NATS2023 = (2215, 2532)
WSBT = (2533,2576)

tournaments = [CCWT, SBST, MIT2021, SBL, LOST, SBST2, DAST, ASS, MIT2022, CAST2022, 
               DASONI2022, PROMETHEUS2022,ESBOT2022, NATS2022, MIT2023, NFSBL,
               IGNIS2023, ESBOT2023, OLYMPUS2023, DASONI2023, NATS2023, WSBT]
names = ["CCWT", "SBST", "MIT2021", "SBL", "LOST", "SBST2", "DAST", "ASS", "MIT2022", "CAST2022", 
               "DASONI2022", "PROMETHEUS2022", "ESBOT2022", "NATS2022", "MIT2023", "NFSBL",
               "IGNIS2023", "ESBOT2023", "OLYMPUS2023", "DASONI2023", "NATS2023", "WSBT"]

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
totalDiff = []
for t in range(len(tournaments)):
    l = tournaments[t][0]
    r = tournaments[t][1]
    for i in teams:
        if abs(float(i[r-1]) - float(i[l-1])) > 0.1:
            add = []
            if float(i[l-1]) < 1:
                add.append(i[0])
                add.append(round(float(i[r-1]) - float(1200),4))
                add.append(names[t])
            else:
                add.append(i[0])
                add.append(round(float(i[r-1]) - float(i[l-1]),4))
                add.append(names[t])
            sortedElo.append(add)

# print(sortedElo)

# sortedElo  = sorted(sortedElo, key = lambda x:x[1], reverse = True)
# print(sortedElo)
for i in sortedElo:
    if(i[0] == "LYNBROOK"):
        print(i[0], i[1], i[2])
