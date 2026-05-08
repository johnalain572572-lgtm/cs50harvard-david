import torch
# a standard data tensor
x_data =torch.tensor([[1.,2.],[3.,4.]])
# a patrameter tensor we need gradients
w = torch.tensor([[1.0],[2.0]],requires_grad=True)
print(f"data tensor requires_grad: {x_data.requires_grad}")
print(f"parameter tensor requires_grad: {w.requires_grad}")
print("-------------------------")
a = torch.tensor(2.0,requires_grad=True)
b = torch.tensor(3.0,requires_grad=True)
x = torch.tensor(4.0,requires_grad=True)
y = a + b
z = x + y
print(f"grad_fn for z: {z.grad_fn}")
print(f"grad_fn for y: {y.grad_fn}")
print(f"grad_fn for a: {a.grad_fn}")
print(y, z)
print("--------------")
#element-wise multiplication('*)
a = torch.tensor([[1,2],[3,4]])
b = torch.tensor([[10,20],[30,40]])
element_wise_product = a * b
print(element_wise_product)
# matrix multiplication using('@)
#powers neural networks
#rule number of columns in 1st matrix must 
# be equal number of row in the 2nd matrix
m1 = torch.tensor([[1,2,3],[4,5,6]])
m2 = torch.tensor([[7,8],[9,10],[11,12]])
matrix_product= m1 @ m2
print(matrix_product)