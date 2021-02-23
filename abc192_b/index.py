s = input()
S = s[1::2]+'A'
s = s[::2]+'a'
print("Yes" if S.isupper() and s.islower() else "No")