from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().splitlines()

l = sorted(lines)

guards = defaultdict(lambda: [0 for x in range(60)])

for s in l:
    if s[25] == "#":
        g = s.split()[3]

    elif s[25] == "a":
        st = int(s[15:17])

    else:
        t = int(s[15:17])

        for x in range(st, t):
            guards[g][x] += 1

# part 1
g1 = sorted(guards.keys(), key=lambda g: -sum(guards[g]))[0]
# part 2
g2 = sorted(guards.keys(), key=lambda g: -max(guards[g]))[0]

for g in [g1, g2]:
    gh = guards[g]
    minute = gh.index(max(gh))
    print(int(g[1:]) * minute)
