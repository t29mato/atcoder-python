H, W = map(int, input().split(' '))
l = list()
for h in range(H):
    s = input().split(' ')
    for w in range(W):
        l.append(int(s[w]))

result = 0
for n in l:
    result += n - min(l)

print(result)

