rounds = int(input())

# 最終的に準優勝したプレイヤーを知る必要があるので、
# プレイヤー一覧を `init_points` としてもっとく
init_points = list(map(int, input().split()))
points = init_points

for round in range(rounds):
    new_points = list()
    # 2 ^ nをするために、ちょっと変わった引き算をしてる。
    # JSなら i-- でインクリメントするところだが、Pythonでのやり方不明につき、ちょっと読みにくいが
    # rounds=4の場合、4^2, 3^2, 2^2, 1^2としてくれる
    for num in range(2 ** (rounds - round)):
        # 欲しいのは準優勝なので、rounds-round=current_roundが最後でない時だけ、
        # 勝ち上がりで判定
        if rounds - round != 1:
            if num % 2 == 0:
                new_points.append(max(points[num:num+2]))
        else:
            new_points.append(min(points[num:num+2]))
    # 次ラウンドでの戦いをまっさらにするため。
    points = new_points

# indexが0から始まるので1を足した
print(init_points.index(points[0]) + 1)