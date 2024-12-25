with open("input.txt", "r") as file:
    connections = file.read().strip().splitlines()

connections = [connection.split("-") for connection in connections]

adjacencies = {}

for c1, c2 in connections:
    if c1 not in adjacencies:
        adjacencies[c1] = set()
    adjacencies[c1].add(c2)
    if c2 not in adjacencies:
        adjacencies[c2] = set()
    adjacencies[c2].add(c1)

cliques = set()

def findClique(pc, connectedTo):
    clique = tuple(sorted(connectedTo))
    if clique in cliques:
        return
    cliques.add(clique)
    for neighbour in adjacencies[pc]:
        if neighbour in connectedTo:
            continue
        conntectedToAll = True
        for connectedpc in connectedTo:
            if neighbour not in adjacencies[connectedpc]:
                conntectedToAll = False
        if not conntectedToAll:
            continue
        copy_set = set(connectedTo)
        copy_set.add(neighbour)
        findClique(neighbour, copy_set)
                
for pc in adjacencies:
    findClique(pc, {pc})

largest_clique = max(cliques, key=len)
answer = ""
for item in largest_clique:
    answer += item + ","

print(answer[:-1])
    

