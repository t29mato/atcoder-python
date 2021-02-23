input = input()

n = int(input.split(' ')[0])
k = int(input.split(' ')[1])

def fn(n, k):
    if k == 0:
        return n
    g1 = int(''.join(sorted(list(str(n)), reverse=True)))
    g2 = int(''.join(sorted(list(str(n)), reverse=False)))
    return fn(g1-g2, k-1)

print(fn(n, k))
