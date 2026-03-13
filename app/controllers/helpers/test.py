import networkx as nx
import itertools
# example data
listA = [{"debit": 600, "credit": 0, "id": 1},{"debit": 0, "credit": 300, "id": 1},         {"debit": 200, "credit": 100, "id": 1},         {"debit": 100, "credit": 50, "id": 1}]
listB = [{"debit": 0, "credit": 300, "id": 1},{"debit": 0, "credit": 300, "id": 1},         {"debit": 100, "credit": 200, "id": 1},         {"debit": 50, "credit": 100, "id": 1},         {"debit": 25, "credit": 50, "id": 1},         {"debit": 75, "credit": 150, "id": 1}]

# create bipartite graph
listA_tuples = [(d['debit'], d['credit'], i) for i, d in enumerate(listA)]
listB_tuples = [(d['debit'], d['credit'], i) for i, d in enumerate(listB)]

# find all combinations of listB that sum to each debit value in listA
matches = {}
for a in listA_tuples:
    matches[a[2]] = []
    for b in listB_tuples:
        if a[0] == b[1] and a[1] == b[0]:
            matches[a[2]].append(b[2])

# find all possible pairings of matches using itertools.product
pairings = list(itertools.product(*matches.values()))

# filter pairings to only include those with unique matches
unique_pairings = []
for p in pairings:
    if len(set(p)) == len(p):
        unique_pairings.append(p)

# print unique pairings
for p in unique_pairings:
    print("Matched pairs:")
    print(i,j)
    for i, j in enumerate(p):
        print(f"ListA[{i}]: {listA[i]} <-> ListB[{j}]: {listB[j]}")
    print()  # empty line for separation