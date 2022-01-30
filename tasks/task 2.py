n, m = (int(x) for x in input().split())

buckets = 0
while True:
    if n < m:
        rib = n
        m -= rib
    else:
        rib = m
        n -= rib

    buckets +=1
    if n == 0 or m == 0:
        break
print(buckets)

# succes!