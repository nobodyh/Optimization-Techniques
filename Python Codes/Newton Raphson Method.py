import numpy as np
from sympy import *
x, y, z,s = symbols('x y z s')
init_printing(use_latex=True)


def fu(x):
    f=float((2*(x**3)/3)+5*x - np.exp(x))
    return f

def fu11(x,dx):

    f1=float(np.divide((fu((x+dx))-fu((x-dx ))),(np.multiply(2,dx))))
    print(fu(x+dx),fu(x-dx),2*dx)
    print("f'(x):",f1,"\n")
    
def fu1(x,dx):
    f1=float(np.divide((fu((x+dx))-fu((x-dx ))),(np.multiply(2,dx))))
    return f1



def fu22(x,dx):
    f2=float((fu(x+dx)+fu(x-dx)-2*fu(x))/(dx**2))
    print(fu(x+dx),fu(x-dx),2*fu(x),dx**2)
    print("f''(x):",f2,"\n")

def fu2(x,dx):
    a=fu(x+dx)
    b=fu(x-dx)
    c=2*fu(x)
    f2=(a+b-c)
    print(f2)
    f3=dx*dx
    print(f2,f3)
    f4=f2/f3
    return f4


e=float(input("Enter the Termination factor(from 10^-4 till 10^-10):"))
x=float(input("Enter Initial Guess: "))
flag=1
i=0

for i in range(3):
    dx=float(np.multiply(0.01,x))
    print("\nx",i+1,":",x," dx:",dx)
    fu11(x,dx)
    fu22(x,dx)
    x= float(x-(np.divide(fu1(x,dx),fu2(x,dx)) ))
    dx=float(np.multiply(0.01,x))
    print("x:",i+2,":",x,"f'(x):",fu1(x,dx))
    
    if(np.abs(fu1(x,dx))<e):
        flag=0
    print("\n")
