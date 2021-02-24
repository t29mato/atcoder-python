glass_count, max_drunk = map(int, input().split())

total = 0
result = -1
for n in range(glass_count):
    volume, percent = map(int, input().split())
    total += volume * percent
    if total > max_drunk * 100:
        result = n + 1
        break

print(result)