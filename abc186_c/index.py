N = int(input())
result = 0
for n in range(1, N+1):
    s8 = str(oct(n))[2:]
    s10 = str(n)
    if '7' in s8:
        continue
    if '7' in s10:
        continue
    result += 1
print(result)
