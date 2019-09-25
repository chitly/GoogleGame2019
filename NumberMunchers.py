c = 0
for i in range(1, 1000):
    for j in range(i, 1000):
        x = i * j
        if x >= 1000:
            break
        s = str(x)
        if len(s) == 1:
            c += 1
            # print(s)
        elif len(s) == 2 and s[0] < s[1]:
            c += 1
            # print(s)
        elif len(s) == 3 and s[0] < s[1] < s[2]:
            c += 1
            # print(s)
print(c)