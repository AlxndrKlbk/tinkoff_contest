n = int(input())
# A = list(set(int(x) for x in input().split()))
A = list(int(x) for x in input().split())
A.sort()


min_val = 1
while True:
    succes = True
    prev = min_val
    i = 0
    for element in A:
        i += 1
        Ak = prev**2 - element
        if Ak < 0:
            succes = False
            break
        elif i == n:
            break
        else:
            prev = Ak

    if succes:
        print(min_val)
        break
    min_val +=1

# succes!