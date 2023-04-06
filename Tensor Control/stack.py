import torch

batch_size, N, K = 3, 10, 256

x = torch.rand(batch_size, N, K) # [M, N, K]
y = torch.rand(batch_size, N, K) # [M, N, K]

output = torch.stack([x, y], dim = 1) # [M, 2, N, K]

print(output.shape)