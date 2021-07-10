import math

def bracket(a,f,s=0.001,m=2):
  """ Finds an interval [a,b] where the function f is unimodal

  Args:
    a: Starting point
    f: Objective function
    s: Initial step size
    m: scaling factor for the step size

  Returns:
    A list with the lower and upper bounds of the interval 
    in wich f is supposedly unimodal 

  """
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
  """ Impelements the Golden Section Serach method
  
    Avriel, M., & Wilde, D. J. (1966). Optimally proof for the symmetric fibonacci search technique. Fibonacci Quarterly Journal, 265-269.
    Kiefer, J. (1953). Sequential minimax search for a maximum. Proceedings of the American mathematical society, 4(3), 502-506.
    
    Args: 
      f: Objective function
      a: Lower bound of the search interval
      b: Upper bound of the search interval
      tol: Tolerance for the minimum point

    Returns:
      The minimum point (with tolerance tol/2) of f in the interval [a,b]
  """


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

def quadratic_fit_search(f,a,b,tol):
  """ Impelements the Quadratic Fit Search method to find the minimum for 
      a single variable function.
  
    
    Args: 
      f: Objective function
      a: Lower bound of the search interval
      b: Upper bound of the search interval
      tol: Tolerance for the minimum point

    Returns:
      The minimum point (with tolerance tol) of f in the interval [a,b]
  """

  c = b
  b = (c-a)/2

  fa = f(a)
  fb = f(b)
  fc = f(c)

  while abs(c-a) < tol:
    x = 0.5*(fa*(b**2-c**2)+fb*(c**2-a**2)+fc*(a**2-b**2))/(fa*(b-c) +fb*(c-a) +fc*(a-b))
    fx = f(x)
    print(x)
    if x > b:
      if fx > fb:
        c = x
        fc = fx
      else: 
        a = b
        fa = fb
        b = x
        fb = fx
    else:
      if fx > fb:
        a = x
        fa = fx
      else:
        c = b
        fc = fb
        b = x
        fb = fx

  return (a+c)/2