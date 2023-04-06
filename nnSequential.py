import torch.nn as nn
import torch.nn.functional as F

class MyNeuralNetwork(nn.Module):
    def __init__(self):
        super(MyNeuralNetwork, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=30, kernel_size=5)
        self.fc1 = nn.Linear(in_features=30*5*5, out_features =128, bias=True)
        self.fc2 = nn.Linear(in_features=128, out_features=10, bias=True)

    def forward(self, x):
        x = F.relu(self.conv1(x), inplace=True)
        x = F.max_pool2d(x, (2, 2))

        x = F.relu(self.conv2(x), inplace =True)
        x = F.max_pool2d(x, (2,2))

        x= x.view(x.shape[0], -1)
        x = F.relu(self.fc1(x), inplace=True)
        x = F.relu(self.fx2(x), inplace=True)

        return x

## nn.Sequential을 사용한 신경망

class MyNeuralNetworkSequenital(nn.Module):
    def __init__(self):
        super(MyNeuralNetworkSequenital, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5),
            nn.ReLU(inplace=True),
            nn.Maxpool2d(2)
        )

        self.layer2 = nn.Sequential(
            nn.conv2d(in_channels=64, out_channels=30, kernel_size =5),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2)
        )

        self.layer3 = nn.Sequential(
            nn.Linear(in_features=30*5*5, out_features=128, bias=True),
            nn.ReLU(inplace=True)
        )

        self.layer4 = nn.Sequential(
            nn.Linear(in_features=128, out_features=10, bias=True),
            nn.ReLU(inplace=True)
        )

    def forward(self, x ):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        return x