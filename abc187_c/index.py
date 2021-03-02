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

c_list = list(set(l_list) & set(r_list))
if len(c_list) > 0:
    print(c_list[0])
else:
    print('satisfiable')
    