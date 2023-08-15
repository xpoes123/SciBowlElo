import os
print (os.getcwd())

elos = {}
gp = {}
matches = []
with open("/Users/davidjiang/cs/fun/elo/data.txt") as f:
    skipping = False
    for line in f:
        if line[0] == "~":
            skipping = bool(input("Press enter if " + line[1:-1] + " should be included in stats: "))
        else:
            if skipping or len(line) < 2:
                continue
            else:
                nl = line[:-1].split("\t")
                nl[0] = nl[0].upper()
                nl[1] = nl[1].upper()
                matches.append(nl)
kp1 = 64
kp2 = 32
k = 16
np1 = 30
np2 = 75
print(len(matches))
for m in matches:
    r = 1
    if m[2] == 'L':
        r = 0
    elif m[2] == 'T':
        r = 0.5
    w = 1200
    l = 1200
    g1 = 0
    g2 = 0
    k1 = k
    k2 = k
    if m[0] in elos:    
        w = elos[m[0]]
    if m[1] in elos:
        l = elos[m[1]]
    if m[0] in gp:
        g1 = gp[m[0]]
    if m[1] in gp:
        g2 = gp[m[1]]
    k1 = kp1 if g1 < np1 else kp2 if g1 < np2 else k
    k2 = kp1 if g2 < np1 else kp2 if g2 < np2 else k
    elos[m[0]] = w + k1*(r-1/(1+10**((l-w)/480)))
    elos[m[1]] = l + k2*((1-r)-1/(1+10**((w-l)/480)))
    gp[m[0]] = g1+1
    gp[m[1]] = g2+1
    
sortedElos = sorted(elos.items(), key=lambda x:-x[1])
print(len(sortedElos))
for j in range(len(sortedElos)):
    i = sortedElos[j]
    # print(str(j+1) + ") " + i[0] + ", " + str(i[1])[:7] + ", " + str(gp[i[0]]))
    print( i[0], str(i[1])[:7], str(gp[i[0]]))