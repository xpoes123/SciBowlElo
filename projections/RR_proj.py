FILE_NAME = "MITRR.txt"

tournament = []
with open("/Users/davidjiang/cs/fun/elo/projections/" + FILE_NAME) as f:
    for line in f:
        bracket = line.split()
        tournament.append(bracket)
        
elos = {}
with open("/Users/davidjiang/cs/fun/elo/projections/elos.txt") as f:
    for line in f:
        team_elo = line.split()
        elos[team_elo[0]] = float(team_elo[1])

RRscores = []
for group in tournament:
    scores = []
    for t1 in group:
        if t1 not in elos:
                elos[t1] = 1200
        scores.append(t1)
        expected_score = -0.5
        for t2 in group:
            if t2 not in elos:
                elos[t2] = 1200
            expected_score += 1/(1+10**((elos[t2]-elos[t1])/400))
        scores.append(expected_score)
    RRscores.append(scores)

for group in RRscores:
    for i in range(0, len(group), 2):
        print(group[i], " Expected Score: ", group[i+1])
    print()

avg_elo = []
for group in tournament:
    sum = 0
    for t in group:
        sum += elos[t]
    avg_elo.append([sum/len(group), len(avg_elo)])

for i in sorted(avg_elo)[::-1]:
    print(f"{i[0]:.2f} Group: {i[1] + 1}")