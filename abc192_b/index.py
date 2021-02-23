s = input()
result = True
for i in range(len(s)):
    if (i+1) % 2 == 1 and s[i].isupper():
        result = False
    if (i+1) % 2 == 0 and s[i].islower():
        result = False

print('Yes' if result else 'No')