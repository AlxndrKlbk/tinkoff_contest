A, B, n = (int(x) for x in input().split())

if A < B:
    print('NO')
elif(A - B)/2 < n:
    print('NO')
else:
    print('YES')

# succes!