import math

high = int(input())
up_dist = list(int(x) for x in input().split())
down_dist = list(int(x) for x in input().split())


jump_counter = 0
succes = False
while True:
    movement = []
    dist_change = []
    for i, val in enumerate(up_dist):
        if val not in movement and val <= high:
            move = up_dist[i] - down_dist[i]
            movement.append(val)
            dist_change.append(move)
            if (high - up_dist[i]) == 0:
                jump_counter += 1
                succes = True
                break
    if succes:
        break
            
    jump_counter += 1
    high -= max(dist_change)


print(jump_counter)