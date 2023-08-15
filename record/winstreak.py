def winStreak(TEAM = None):
    ws = 0
    ls = 0
    if TEAM:
        name = TEAM
        name2 = TEAM
        tws = 0
        tls = 0
        for i in teams[teamsDict.get(TEAM)]:
            if i == 1:
                tws += 1
                tls = 0
            elif i == 0:
                tls += 1
                tws = 0
            ws = max(ws, tws)
            ls = max(ls, tls)
    else:
        for i in teams:
            val = winStreak(i[0])
            if ws < val[1]:
                name = i[0]
            ws = max(ws, val[1])
            if ls < val[2]:
                name2 = i[0]
            ls = max(ls, val[2])
    return name, ws, ls, name2

teams = []
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
        teams.append([name])
        teamsDict[name] = index
        index += 1

matches = []
with open("/Users/davidjiang/cs/fun/elo/data.txt") as f:
    for line in f:
        nl = line[:-1].split("\t")
        nl[0] = nl[0].upper()
        nl[1] = nl[1].upper()
        matches.append(nl)

for i in matches:
    t1 = teams[teamsDict.get(i[0])]
    t2 = teams[teamsDict.get(i[1])]
    if(i[2] == "W"):
        t1.append(1)
        t2.append(0)
    elif(i[2] == "L"):
        t1.append(0)
        t2.append(1)
    else:
        t1.append(0.5)
        t2.append(0.5)

print(winStreak(TEAM = "FOOTHILL"))
# print(winStreak())

# ws = []
# ls = []
# for i in teamsDict:
#     add = [i]
#     add2 = [i]
#     ret = winStreak(TEAM = i)
#     add.append(ret[1])
#     add2.append(ret[2])
#     ws.append(add)
#     ls.append(add2)
# ws = sorted(ws, key = lambda x:x[1], reverse=True)
# ls = sorted(ls, key = lambda x:x[1], reverse=True)
# # for i in range(len(ws)):
# #     print(ws[i])

# # for i in range(len(ls)):
# #     print(ls[i])

# for i in range(10):
#     print(ws[i])
# print("$$$$$$$$$$$$$$$$$$")
# for i in range(10):
#     print(ls[i])