import numpy as np
 
def fibonacci_sequence(n):
    if n < 0:
        print('Negative Value Encountered')
        pass
    
    if n in {0,1}:
        return n
    
    return (fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2))    
    
def function(x):
    if(x == 0):
        x = np.divide(1,np.power(10,12))
    
    expression = float(x**2 + 54/x)
    return expression


a, b, e, n = (float(input("Enter a: ")),
              float(input("Enter b: ")),
              float(input("Enter the Termination Factor: ")),
              int(input("Enter desired number of function evaluations: ")))

L = (b - a)

i, k = 0, 2


while(k != (n + 1)):
    
    L_k = np.multiply(np.divide(fibonacci_sequence(n - k + 1), fibonacci_sequence(n + 1)), L)
    x_1, x_2 = a + L_k, b - L_k
    
    if(function(x_1) < function(x_2)):
        b = x_2; L_k = b - a
   
    elif(function(x_2) < function(x_1)):
        a = x_1; L_k = b - a
    
    else:
        a, b = x_1,x_2 
        L_k = b - a
    
    print(f"\nIteration {i + 1}:\nF(n - k + 1): {fibonacci_sequence(n - k + 1)} F(n + 1):{fibonacci_sequence(n + 1)} L:{L} Lk:{L_k}\n(x1, x2):({x_1}, {x_2})\n(a, b): ({a}, {b})")
  
    i += 1; k += 1
    
print(f"\nNo.of Iterations performed: {i}")
print(f"\nFinal interval lies at ({a}, {b}) at the end of {i} iterations.")
