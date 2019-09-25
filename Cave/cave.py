h = 30
w = 51
st = (1, 25)
tg = (29, 25)
cave = []
for i in range(h):
    cave.append(input())
queue = [(st[0], st[1], 0, [])]
q_len = 1
q_idx = 0
visited = {}
fin = False
while q_idx < q_len:
    x, y, z, s = queue[q_idx]
    # print(x, y, z ,s)
    # if fin: break
    if (x, y) in visited:
        if visited[(x, y)] > z:
            visited[(x, y)] = z
        else:
            q_idx += 1
            continue
    visited[(x, y)] = z
    # up
    # print('up', cave[x - 1][y])
    if cave[x - 1][y] == ' ':
        t = 0
        for i in range(x - 1, -1, -1):
            if cave[i][y] == 'B':
                queue.append((i + 1, y, z + 60 + t, s + ['u']))
                break
            elif (i, y) == tg:
                print(z + t + 1, ''.join(s))
                fin = True
            t += 1
    # down
    # print('down', cave[x + 1][y])
    if cave[x + 1][y] == ' ':
        t = 0
        for i in range(x + 1, h, 1):
            if cave[i][y] == 'B':
                queue.append((i - 1, y, z + 60 + t, s + ['d']))
                break
            elif (i, y) == tg:
                print(z + t + 1, ''.join(s))
                fin = True
            t += 1
    # left
    # print('left', cave[x][y - 1])
    if cave[x][y - 1] == ' ':
        t = 0
        for i in range(y - 1, -1, -1):
            if cave[x][i] == 'B':
                queue.append((x, i + 1, z + 60 + t, s + ['l']))
                break
            elif (x, i) == tg:
                print(z + t + 1, ''.join(s))
                fin = True
            t += 1
    #right
    # print('right', cave[x][y + 1])
    if cave[x][y + 1] == ' ':
        t = 0
        for i in range(y + 1, w, 1):
            if cave[x][i] == 'B':
                queue.append((x, i - 1, z + 60 + t, s + ['r']))
                break
            elif (x, i) == tg:
                print(z + t + 1, ''.join(s))
                fin = True
            t += 1
    q_idx += 1
    q_len = len(queue)
    # print(queue)