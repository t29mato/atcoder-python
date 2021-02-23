A, B, C = map(int, input().split())
# A=Takahashi, B=Aoki
if C == 1: # Aoki君が選手
    print('Aoki' if A < B else 'Takahashi')
else:
    print('Takahashi' if A > B else 'Aoki')
