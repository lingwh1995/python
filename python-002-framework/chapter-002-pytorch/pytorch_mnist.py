"""
pip install torch torchvision torchaudio
"""
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms

train_data =datasets.MNIST(
    root = 'mnist',
    train = True,
    transform = transforms.ToTensor(),
    download=True
)

test_data = datasets.MNIST(
    root = 'mnist',
    train = False,
    transform = transforms.ToTensor(),
    download = True
)
print(train_data)
print(test_data)