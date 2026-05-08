import torch
#expert selection : torch.gather()function
data = torch.tensor([[10,11,12,13],
                    [20,21,22,23],
                    [30,31,32,34]])
indices_to_select =torch.tensor([[2],[0],[3]
                                 ])
# dim=1 select rows
selected_values =torch.gather(data, dim=1,index= indices_to_select)
print(selected_values)#out:
#   tensor([[12],
        # [20],
        # [34]])