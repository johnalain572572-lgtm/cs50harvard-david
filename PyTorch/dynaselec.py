#find the index of higher vales
import torch
scores = torch.tensor([[10,0,5,20,1],
                       [1,30,2,5,0]])
best_indices = torch.argmax(scores, dim=1)
print(best_indices)#tensor([3, 1])