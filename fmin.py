from os import name
import numpy as np
import line_search as ls


def perform_line_search(x,f,s,line_search,tol):
    f_aux = lambda a : f(x + a*s)
    bracket = ls.bracket(0,f_aux)
    alpha = line_search(f_aux,bracket[0],bracket[1],tol=tol)
    return alpha

def powell(x,f,tol=1e-6,line_search=ls.quadratic_fit_search):

    lx = [x]
    lfx = [f(x)]
    directions = []

    for i in range(len(x)):
        directions.append(np.zeros(len(x)))
        directions[i][i] = 1

    s = directions[-1]
    alpha = perform_line_search(x,f,s,line_search,tol)
    x = x + alpha*s

    lx.append(x)
    lfx.append(f(x))

    while np.linalg.norm(s) > tol:

        z = x
        i = 0

        while i < len(x) and np.linalg.norm(s) > tol:
            
            s = directions[i]
            alpha = perform_line_search(x,f,s,line_search,tol)
            x = x + alpha*directions[i]

            lx.append(x)
            lfx.append(f(x))

            i = i+1

        s = x - z
        alpha = perform_line_search(x,f,s,line_search,tol)
        x = x + alpha*s

        lx.append(x)
        lfx.append(f(x))

        directions.pop(0)
        directions.append(s)

    return x,f(x),lx,lfx



def gradient_descent(x,f,grad,tol=1e-6,alpha=[],line_search=ls.quadratic_fit_search):

  lx = [x]
  lfx = [f(x)]

  got_alpha = True if alpha else False 

  gradx = grad(x)

  while np.linalg.norm(gradx) > tol:

    if not got_alpha:
      f_aux = lambda a : f(x - a*gradx)
      bracket = ls.bracket(0,f_aux)
      alpha = line_search(f_aux,bracket[0],bracket[1],tol=tol)
      
    x = x - alpha*gradx
    gradx = grad(x)

    lx.append(x)
    lfx.append(f(x))

  return x,f(x),lx,lfx


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
    


