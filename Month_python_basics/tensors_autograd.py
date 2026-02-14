import torch

#creating a tensor with requires_grad=True to track computations

x = torch.tensor([[2.0,3.0],[4.0,5.0]], requires_grad=True)
print("Tensor x:\n", x )

# performing some operations on the tensor

y = x * 2 
z = y.mean()
print("Tensor y:\n", y)
print("Tensor z= mean(y)\n", z.item())

#-- Autograd Basics ---
#backpropagating the gradients
z.backward()

print("Gradient of z with respect to x (dz/dx):\n", x.grad)

#define a simple function f(x) = x^2 and compute its gradient
x2= torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
f = x2**2 +3*x2
print(" f(x) = x^2 + 3x evaluated at x2:\n", f)

#sum to get scalar output

loss = f.sum()
print("Loss (sum of f):\n", loss.item())    
loss.backward()
print("Gradient of loss with respect to x2 (d(loss)/dx2):\n", x2.grad)