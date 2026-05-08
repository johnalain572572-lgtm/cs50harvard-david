import torch
scores = torch.tensor([[10.,20.,30.0],[5.,10.,15]])
avg_per_asignment=scores.mean(dim=0)
avg_per_stydent=scores.mean(dim=1)
print(avg_per_asignment)
print(avg_per_stydent)