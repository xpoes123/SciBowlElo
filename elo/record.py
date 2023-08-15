from operator import itemgetter
matches = []
records = []
teams = []
with open("/Users/davidjiang/cs/fun/elo/data.txt") as f:
    for line in f:
        nl = line[:-1].split("\t")
        nl[0] = nl[0].upper()
        nl[1] = nl[1].upper()
        matches.append(nl)
    for m in matches:
        if m[0] in teams:
            if m[2] == 'L':
                records[teams.index(m[0])][2] += 1
            elif m[2] == 'T':
                records[teams.index(m[0])][3] += 1
            else:
                records[teams.index(m[0])][1] += 1
        else:
            teams.append(m[0])
            records.append([m[0], 0,0,0,0,0])
            if m[2] == 'L':
                records[teams.index(m[0])][2] += 1
            elif m[2] == 'T':
                records[teams.index(m[0])][3] += 1
            else:
                records[teams.index(m[0])][1] += 1
        if m[1] in teams:
            if m[2] == 'L':
                records[teams.index(m[1])][1] += 1
            elif m[2] == 'T':
                records[teams.index(m[1])][3] += 1
            else:
                records[teams.index(m[1])][2] += 1
        else:
            teams.append(m[1])
            records.append([m[1], 0,0,0,0,0])
            if m[2] == 'L':
                records[teams.index(m[1])][1] += 1
            elif m[2] == 'T':
                records[teams.index(m[1])][3] += 1
            else:
                records[teams.index(m[1])][2] += 1
        records[teams.index(m[0])][5] += 1
        records[teams.index(m[1])][5] += 1

for i in records:
    print(i)
    i[4] = (i[1]/(i[5]))
records = [i for i in records if i[5] > 20]

records = sorted(records, key = itemgetter(4, 5), reverse=True)
for i in records:
    print(i[0], i[1], i[2])