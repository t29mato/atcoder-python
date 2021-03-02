a, b = map(str, input().split())

sum_a = sum(list(map(int, a)))
sum_b = sum(list(map(int, b)))

print(max(sum_a, sum_b))