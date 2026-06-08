import torch

print("CUDA:", torch.cuda.is_available())

x = torch.randn(10000, 10000)

print("Tensor created")
print(x.shape)