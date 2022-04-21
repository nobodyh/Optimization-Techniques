import numpy as np

def function(x):
    if(x == 0):
        x = np.divide(1,np.power(10,12))
    
    expression = float(np.add(np.power(x,2),np.divide(54,x)))
    
    return expression

def delta():
    flag = 0
    
    while(flag == 0):
        x_0 = float(input("Enter the Initial Guess: "))
        dx = float(input("Enter the dx: "))
        
        if(function(x_0 - np.abs(dx)) >= function(x_0) and function(x_0) >= function(x_0 + np.abs(dx))):
            flag += 1
            
            return x_0, dx
        
        elif(function(x_0 - np.abs(dx)) <= function(x_0) and function(x_0) <= function(x_0 + np.abs(dx))):
            flag += 1
            
            return x_0, (-dx)

x_0, dx = delta()

k = 0

flag = False

i = 0

while(flag == False):
    
    x_1 = np.add(x_0, np.multiply(np.power(2,k),dx))
    
    if(function(x_1) < function(x_0)):
        k += 1
        x_0 = x_1
        x_1 = np.add(x_0, np.multiply(np.power(2, k),dx))
        
        print(f"Iteration {i + 1}: x_0: {np.around(x_0, 4)} and x_1: {np.around(x_1, 4)}")
        
    else:
        print(f"\nMinimum lies in ({np.around(np.subtract(x_0, np.multiply(np.power(2, k-1), dx)), 4)},{np.around(x_1, 4)})")
        
        flag = True
    i += 1
print(f"\nNo.of Iterations performed: {i}")
