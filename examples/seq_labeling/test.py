import numpy as np
import torch
import torch.nn as nn
from PIL import Image
from torch.autograd import Variable
from torchvision import models, transforms
import cv2

img_path = 'G:/054/unilm/layoutlm/layoutlm/data/1.jpg'
feature_path = 'G:/054/unilm/layoutlm/image_feature/00040534.txt'
'''class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = models.resnet101(pretrained=True, progress=True)

        def save_output(module, input, output):
            self.buffer = output
        self.model.layer4.register_forward_hook(save_output)

    def forward(self, x):
        self.model(x)
        return self.buffer
'''
transform1 = transforms.Compose([
    transforms.ToTensor()]
)

img = Image.open(img_path)
print(type(img))
img = np.array(img)
img1 = cv2.imread(img_path)
print(type(img))
# img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = Image.fromarray(img)
img.show()
print(img.size)

img1 = transform1(img)
print(img1.shape)

resnet = models.resnet101(pretrained=True)
fc_features = resnet.fc.in_features
resnet.fc = nn.Linear(fc_features, 768)
x = Variable(torch.unsqueeze(img1, dim=0).float(), requires_grad=False)
# y1 = resnet18(x)
y = resnet(x)
y = y.data.numpy()
y = np.squeeze(y)
np.savetxt(feature_path, y, delimiter=',')
# y3 = resnet152(x)
# y4 = densenet201(x)

y_ = np.loadtxt(feature_path, delimiter=',').reshape(1, 2048)