n, k = map(int, input().split())

result = n
for _ in range(k):
    result = int(''.join(sorted(list(str(result)), reverse=True))) - int(''.join(sorted(list(str(result)), reverse=False)))

print(result)
