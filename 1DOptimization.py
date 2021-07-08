import math

def bracket(a,f,s=0.01,m=2):

    bracket = [a]

    b = a + s
    bracket = [a,b]

    fa = f(a)
    fb = f(b)

    if fa >= fb :
    
        c = b + s
        fc = f(c)

        while fc < fb:
            b = c
            fb = fc
            s = s*m
            c = c + s
            fc = f(c)

        bracket = [a,c]

    elif fa < fb :
        c = a - s
        fc = f(c)
        while fc < fa:
            a = c
            fa = fc
            s = s*m
            c = c -  s
            fc = f(c)

        bracket = [c,b] 

    return bracket

def golden_search(f,a,b,tol):

  gr = (1 + math.sqrt(5))/2

  c = b - (b-a)/gr
  d = a + (b-a)/gr

  while abs(b-a) > tol:
    if f(c) > f(d):
      a = c
    else:
      b = d
      
    c = b - (b-a)/gr
    d = a + (b-a)/gr

    
  return (b+a)/2
