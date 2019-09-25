coin = 0
for i in range(1, 1001):
    if i % 15 == 0:
        coin += 10 * i
    elif i % 5 == 0:
        coin += 3 * i
    elif i % 3 == 0:
        coin += 2 * i
    else:
        coin += i
print(coin)