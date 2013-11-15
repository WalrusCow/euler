li = []
for x in range(64, 9**5 * 6):
    y = x
    s = x
    p = 0
    while y:
        p = y % 10
        s -= (p**5)
        y = int(y/10)
        if s < 0:
            break
    if not s:
        li.append(x)
print(sum(li))
