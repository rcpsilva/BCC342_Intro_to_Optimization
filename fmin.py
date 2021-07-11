from os import name
import numpy as np
import line_search as ls

def gradient_descent(x0,f,grad,tol=1e-6,alpha=[],line_search=ls.quadratic_fit_search):

    x = np.array(x0)

    # Store x at each generation for later visualization
    list_x = [x]
    list_fx = [f(x)]

    while np.linalg.norm(grad(x)) > tol:

        if not alpha:
            fline = lambda a: f(x - a*np.array(grad(x)))
            bracket = ls.bracket(0,fline)
            alpha = line_search(fline,bracket[0],bracket[1])

        x = x - alpha*np.array(grad(x))
        
        list_x.append(x)
        list_fx.append(f(x))

    return x,f(x),list_x,list_fx

def newton_method(x0,f,grad,H,tol=1e-6):
    
    x = np.array(x0)

    # Store x at each generation for later visualization
    list_x = [x]
    list_fx = [f(x)]

    while np.linalg.norm(grad(x)) > tol:
        
        hinv = np.linalg.inv(H(x))
        g = np.array([grad(x)]).T
        delta = np.matmul(hinv,g)
        x = x - delta.T
        x = x[0]
        
        list_x.append(x)
        list_fx.append(f(x))

        g = grad(x)

    return x,f(x),list_x,list_fx

if __name__ == "__main__":
    
    # Quadratic function with interaction term

    #f = lambda x: x[0]**2 + x[1]**2 + x[0]*x[1]
    #grad = lambda x: [2*x[0] + x[1], 2*x[1] + x[0]]
    #H = lambda x: [[2,1],[1,2]]

    # Rosenbrocks function

    f = lambda x: (100*(x[1] - x[0]**2)**2 + (x[0]-1)**2) 
    grad = lambda x: [-400*(x[1]-x[0]**2)*x[0] + 2*(x[0]-1), 200*(x[1]-x[0]**2)]
    H = lambda x: [[-400*x[1]+1200*x[0]**2,-400*x[0]],[-400*x[0],200]]

    #xs,fs,xlist,fx_list = gradient_descent([1,-2],f,grad)

    xs,fs,xlist,fx_list = newton_method([1,-2],f,grad,H)

    print(xs)
    print(xlist)
    


