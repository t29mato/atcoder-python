N = int(input())
xy = tuple(tuple(map(int, input().split())) for _ in range(N))

result = 0
for i in range(N):
    for j in range(i+1, N):
        xi, yi = xy[i]
        xj, yj = xy[j]
        if -1 <= (yj - yi) / (xj - xi) <= 1:
            result += 1

print(result)