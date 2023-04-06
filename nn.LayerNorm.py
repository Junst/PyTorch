import torch
import torch.nn as nn
import torch.nn.functional as F


input = torch.randn(20, 5, 10, 10) # 학습 가능한 매개변수
m = nn.LayerNorm(input.size()[1:])
m = nn.LayerNorm(input.size()[1:], elementwise_affine = False)
m = nn.LayerNorm([10, 10]) ## 크기 10의 마지막 치수를 통해 Normalization
m = nn.LayerNorm(10)
output = m(input)

print(output)