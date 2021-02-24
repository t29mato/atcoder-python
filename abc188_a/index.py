import numpy as np

X, Y = map(int, input().split())
print('Yes' if np.abs(X - Y) < 3 else 'No')