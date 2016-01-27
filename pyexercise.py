import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( 20*sy.exp(-x**5), (x,0, sy.oo))
    return ans

def my_solution():
    z = np.random.random(100) #create 100 random numbers
    A = np.reshape(z,(10,10)) 
    b = np.random.random(10)
    b = np.reshape(b,(10,1))
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x

if __name__ == '__main__':
    your_id = 1204052
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
