n, m = (int(x) for x in input().split())

step = 3
i = 0
while True:
    if n == 4 + step*i:
        print(2 + step*i)
        break
    elif n < 4 + step*i:
        print(0)
        break
    i += 1

# succes!