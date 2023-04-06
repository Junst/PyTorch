import torch
import torch.nn as nn

'''
class DenseBlock(nn.Module):
	def __init__(self, in_dim, out_dim):
		super(DenseBlock, self).__init__()
		self.dense = nn.Linear(in_dim, out_dim)
		self.relu = nn.ReLU() # activation function

	def forward(self, x):
		out = self.relu(self.dense(x))
		return out


class OurModel(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim):
        super(OurModel, self).__init__()
        self.linear1 = DenseBlock(in_dim, hidden_dim)
        self.linear2 = DenseBlock(hidden_dim, out_dim)

    def forward(self, x):
        out = self.linear1(x)
        out = self.linear2(out)
        return out


if __name__ == "__main__":
    x = torch.rand(500, 128) # The number of traning sample=500
    model = OurModel(in_dim=128, hidden_dim=64, out_dim=1)
    y = model(x)
    print(y.shape)
'''
#############################
import torch
import torch.nn as nn
import torch.nn.functional as F


class OurModel(nn.Module):
	def __init__(self, in_dim, hidden_dim, out_dim):
		super(OurModel, self).__init__()
		self.linear1 = nn.Linear(in_dim, hidden_dim)
		self.linear2 = nn.Linear(hidden_dim, out_dim)

	def forward(self, x):
		out = F.relu(self.linear1(x))  # activation
		out = F.relu(self.linear2(out))  # activation
		return out


if __name__ == "__main__":
	x = torch.rand(500, 128)  # The number of traning sample=500
	model = OurModel(in_dim=128, hidden_dim=64, out_dim=1)
	y = model(x)
	print(y.shape)