mymap = []
for j in range(0, 12):
    mymap.append(['N'] * 6)


def printMap():
    for x in range(11, -1, -1):
        print(mymap[x])


def fall(a, c):
    j = 12
    while mymap[j-1][c] == 'N' and j > 0:
        j = j - 1
    mymap[j][c] = a

# from collections import deque
# def checkChain(graph, vertex):
    # queue = deque([vertex])
    # level = {vertex: 0}
    # parent = {vertex: None}
    # i = 1
    # while queue:
    #   v = queue.popleft()
    #   for n in graph[v]:
    #     if n not in level:
    #       queue.append(n)
    #       level[n] = i
    #       parent[n] = v
    #   i += 1
    # return level, parent


def checkChain():
    # CodeHere


for i in range(0, 1):
    a, b, r, c = [e for e in input().split()]
    c = int(c)
    if r == 'H':
        fall(a, c)
        fall(b, c+1)
    elif r == 'V':
        fall(a, c)
        fall(b, c)

printMap()
