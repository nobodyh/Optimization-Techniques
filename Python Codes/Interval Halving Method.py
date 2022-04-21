import numpy as np

def function(x):
    if(x == 0):
        x = np.divide(1,np.power(10,12))
    
    expression = float((100-x)**2)
    
    return expression

a, b, e = (float(input("Enter a: ")),
           float(input("Enter b: ")),
           float(input("Enter the Termination Factor: ")))

L_0 = (b - a); L = L_0

i = 0

while(np.abs(L) > e):
    
    xm = np.divide(np.add(a,b),2); fxm = function(xm)
    
    x1 = np.add(a,np.divide(L,4)); x2 = np.subtract(b,np.divide(L,4))
    
    fx1 = function(x1); fx2 = function(x2)
    
    if(fx1 < fxm):
        b = xm; xm = x1; L = (b - a)
    
    elif(fx2 < fxm):
        a = xm; xm = x2; L = (b - a)
    
    else:
        a = x1; b = x2; L = (b - a)
        print(f"\nx1,x2: ({x1}, {x2})")
        print(f"fx1,fx2: ({fx1}, {fx2})")
    
    print(f"\nIteration {i+1}: (a, b): ({a}, {b}); L: {L}")
    
    i += 1
    
print(f"\nNo.of Iterations performed: {i}")
