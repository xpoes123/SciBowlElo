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
    print(mset)
    for line in mset:
        add = []
        name = line.rstrip('\n')
        teams.append([name, 0])
        teamsElo.append([name, 0])
        teamsDict[name] = index
        index += 1

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
                    # j.append(0)
                for k in inbetween:
                    teams[teamsDict.get(k[0])][match+1] = k[1]
                    teamsElo[teamsDict.get(k[0])][1] = k[1]
                # tempteamsElo = [i for i in teamsElo]
                # for j in teams:

                inbetween = []
                continue
            inbetween.append(i)

        for j in teams:
            for k in j:
                p.write(str(str(k) + " "))
            p.write("\n")