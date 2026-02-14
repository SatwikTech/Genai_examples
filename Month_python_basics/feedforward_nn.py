import torch
import torch.nn as nn
import torch.optim as optim

#defining a simple feedforward neural network
class SimpleNN(nn.Module):
    def __init__(self,input_size,hidden_size,output_size):
        super(SimpleNN,self).__init__()
        self.fc1 = nn.Linear(input_size,hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size,output_size)

    def forward(self,x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out
    
#hypper paramaters

input_size=3
hidden_size=5
output_size=1
learning_rate=0.01

#creating a model

model = SimpleNN(input_size,hidden_size,output_size)

#dummy data 

x = torch.tensor([[1.0,2.0,3.0],[4.0,5.0,6.0]],requires_grad=True)
y = torch.tensor([[1.0],[2.0]],requires_grad=True)

#loss function activating and optimizer

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(),lr=learning_rate)

#forward passing 

outputs =model(x)
loss = criterion(outputs,y)
print("predicted outputs:\n",outputs)
print("loss:\n",loss.item())

#backward pass and optimization

optimizer.zero_grad() #clear previous gradients
loss.backward()  # compute gradients
optimizer.step() #update weights parameters

print("updated model parmeters")
for name,param in model.named_parameters():
    print(name,param.data)
