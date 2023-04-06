import numpy as np
import torch

# Case 1 : 같은 크기의 행렬
m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
print(f'shape : m1 = {m1.shape}, m2 = {m2.shape}')
m3 = m1 + m2
print(m3, m3.shape)

# Case 2 : Vector와 행렬
m4 = torch.FloatTensor([[1, 2]])
m5 = torch.FloatTensor([3]) # [3] => [3, 3]
print(f'shape: m4 = {m4.shape}, m5 = {m5.shape}')
m6 = m4 + m5
print(m6, m6.shape)

# Case 3 : 크기가 다른 두 개의 행렬
m7 = torch.FloatTensor([[1, 2]])
m8 = torch.FloatTensor([[3], [4]])
print(f'shape: m7 = {m7.shape}, m8 = {m8.shape}')
m9 = m7 + m8
print(m9, m9.shape)