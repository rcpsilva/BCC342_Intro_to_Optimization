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


f = lambda x: (x+2)**2

b = bracket(1,f)

print(b)