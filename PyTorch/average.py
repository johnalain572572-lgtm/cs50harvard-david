import torch
scores = torch.tensor([[10.,20.,30.0],[5.,10.,15]])
average_score = scores.mean()
print(f"Overall mean: {average_score}")#output:Overall mean: 15.0#lets look at the default behavior