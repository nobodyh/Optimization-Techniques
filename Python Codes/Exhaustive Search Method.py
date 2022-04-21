import numpy as np

def function(x):
    if(x == 0):
        x = np.divide(1,np.power(10,12))
    
    expression = float(np.add(np.power(x,2),np.divide(54,x)))
    
    return expression

a, b, n = (float(input("Enter a: ")), 
           float(input("Enter b: ")), 
           int(input("Enter the number of intermediate points: ")))


dx = float(np.divide(np.subtract(b, a), n))

dx = np.abs(dx)

flag = False

i = 0

x_1 = a; x_2 = x_1 + dx; x_3 = x_2 + dx

while(flag == False):
    if(function(x_1) >= function(x_2) and function(x_2) <= function(x_3)):
        flag = True
        print(f"\nMinimum lies in ({np.around(x_1, 4)}, {np.around(x_3, 4)})")
        break
    
    x_1 = x_2; x_2 = x_1 + dx; x_3 = x_2 + dx
    
    
    
    if(x_3 > b):
        flag = True
        print(f"\nNo minimum or minimum lies at boundary points {np.around(a, 4)} and {np.around(b, 4)}")
        break
    
    i += 1
    print(f"\n Iteration No.{i + 1}: x_1: {np.around(x_1, 4)}, x_2: {np.around(x_2, 4)}, x_3: {np.around(x_3, 4)}")
    
print(f"\nNo.of iterations taken: {i + 1}")
