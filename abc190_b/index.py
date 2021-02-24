magics, boss_time, boss_damage = map(int, input().split())

result = 'No'
for magic in range(magics):
    time, damage = map(int, input().split())
    if time >= boss_time or damage <= boss_damage:
        continue
    else:
        result = 'Yes'

print(result)