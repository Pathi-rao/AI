class SiameseNetwork(nn.Module):

    def __init__(self, lastLayer = False, pretrained = True):

        super(SiameseNetwork, self).__init__()

        # 3 channel 150*150
        self.conv1 = nn.Conv2d(3, 64, 10)
        self.conv2 = nn.Conv2d(64, 128, 7)
        self.conv3 = nn.Conv2d(128, 128, 4)
        self.conv4 = nn.Conv2d(128, 256, 4)
        # self.fc1 = nn.Linear(30976, 4096)

    def forward(self, x):

        out = F.relu(F.max_pool2d(self.conv1(x), 2))
        print("print-1:")
        print(out.shape)
        out = F.relu(F.max_pool2d(self.conv2(out), 2))
        print("print-2:")
        print(out.shape)
        out = F.relu(F.max_pool2d(self.conv3(out), 2))
        print("print-3:")
        print(out.shape)
        out = F.relu(self.conv4(out))
        print("print-4:")
        print(out.shape)

        out = out.view(out.shape[0], -1)
        print("print-5:")
        print(out.shape)
        out = (self.fc1(out))

        return out

model = SiameseNetwork()
x = torch.ones(4, 3, 150, 150)
model(x)