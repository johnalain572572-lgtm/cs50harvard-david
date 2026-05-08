import torch
data =[[1,2,3],[4,5,6]]
my_tensor =torch.tensor(data)
print(my_tensor)
print("================")
shape = (2,3)
ones = torch.ones(shape)
zeros = torch.zeros(shape)
random = torch.randn(shape)
print(f"Random Tensor:\n {random}")
print("==============")
# creation by mimicking another Tensor
# mimicking تقليد
template =torch.tensor([[1,2],[3,4]])
rand_like = torch.randn_like(template,dtype=torch.float)
print(f"template tensor:\n {template}")
print(f"random_like tensor : \n {rand_like}")
print("---------------")
import torch
tensor = torch.randn(2,3)
print(f"Shape: {tensor.shape}")
# .shape a tuple describing the dimensions your #1 debugging tool
#90 of errors in PyTorch will be shape mismatching
print(f"Datatype: {tensor.dtype}")
# .dtype the data type of the numbers. the default is float32
#its system called AUTOGRAD stands for automatis differentiation
# pytorch comes with built-in gradient calculator
print(f"Device: {tensor.device}")
#.device where the tensor lives cpu or cuda(GPU)
