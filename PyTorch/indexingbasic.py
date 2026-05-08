import torch
x = torch.arange(12).reshape(3,4)
col_2 = x[:,2]
print(col_2)#tensor([ 2,  6, 10])
print(x)#output:
#  tensor([[ 0,  1,  2,  3],
        # [ 4,  5,  6,  7],
        # [ 8,  9, 10, 11]])