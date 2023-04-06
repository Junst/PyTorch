import torch
batch_size, N, K = 3, 10, 256
x = torch.rand(batch_size, N, K) # [M, N, K]
y = torch.rand(batch_size, N, K) # [M, N, K]

output1 = torch.cat([x, y], dim=1) # [M, N+N, K]
output2 = torch.cat([x, y], dim=2) # [M, N, K+K]

print(output1.shape)
print(output2.shape)