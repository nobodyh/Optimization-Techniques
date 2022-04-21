import numpy as np

def function(x):
    if(x == 0):
        x = np.divide(1,np.power(10,12))
    
    expression = float(np.exp(-x)-np.cos(x))
    
    return expression

def fuw(w, a, b):
    return function(float(a + w * (b - a)))

a, b, e = (float(input("Enter a: ")),
           float(input("Enter b: ")),
           float(input("Enter the Termination Factor: ")))

L_0 = (b - a)

i = 0
aw = 0; bw = 1

L = (bw - aw)

while(np.abs(L) > e):
    
    x_1 = float(aw + (0.618)*L); x_2 = float(bw - (0.618)*L) # Phi/Golden Ratio = ((1 + 5**(0.5)) / 2)
    
    fx1 = fuw(x_1, a, b); fx2 = fuw(x_2, a, b)

    print(f"Iteration {i}: (aw,bw): ({aw}, {bw}) L: {L}")

    print(f"w1: {x_1}; w2: {x_2}")

    print(f"f(w1): {np.around(fx1, 4)}; f(w2): {np.around(fx2, 4)}")
    
    if(fx1 > fx2):
        aw = aw
        bw = x_1
        L = (bw - aw)

    elif(fx1 < fx2):
        aw = x_2
        L = (bw - aw)
    
    else:
        aw = x_1
        bw = x_2
        L = (bw - aw)
    
    print(f"\nTherefore (aw, bw): ({aw}, {bw})")
   
    i += 1

print(f"\nNo.of Iterations performed: {i}")
print(f"\nMinimum lies at ({(b - a) * aw}, {(b - a) * bw})")
