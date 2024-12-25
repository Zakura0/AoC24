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

for conn in adjacencies:
    for neighbour in adjacencies[conn]:
        for neighbour2 in adjacencies[neighbour]:
            if neighbour2 != conn and neighbour2 in adjacencies[conn]:
                cliques.add(tuple(sorted([conn, neighbour, neighbour2])))

result = 0

for clique in cliques:
    for pc in clique:
        if pc.startswith("t"):
            result += 1
            break

print(result)

    

