N = int(input())

l_list = list()
r_list = list()
array = list()
for n in range(N):
    s = input()
    if s[0] != '!':
        l_list.append(s)
    else:
        r_list.append(s[1:])

for s in l_list:
    if s in r_list:
        print(s)
        break
else:
    print('satisfiable')