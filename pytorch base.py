import torch.nn as nn
import torch.nn.functional as F

class Model_Name(nn.Module):
    def __init__(self):

        super(Model_Name, self).__init__()
        self.module1 = # ..
        self.module2 = # ..

        '''
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)
        '''

    def forward(self, x):
        x = some_function1(x)
        x = some_function2(x)

        '''
        x= F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        '''
        return x

model = Model_Name() # 여기에 변수를 넣어주면 된다.