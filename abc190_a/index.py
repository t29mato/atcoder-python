A, B, C = map(int, input().split())
# A=Takahashi, B=Aoki
if C == 1: # Aoki君が選手
    print('Aoki' if A < B else 'Takahashi')
else:
    print('Takahashi' if A > B else 'Aoki')

# 勝敗が分かれるのは、高橋君と青木君の飴の数が同じ時だけなので、
# その時だけ、先手がどちらかを見て決める回答でも良い。（haijimaさんの回答がそうなってた）