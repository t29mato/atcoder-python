N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for n in range(N):
    result += A[n] * B[n]

print('Yes' if result == 0 else 'No')