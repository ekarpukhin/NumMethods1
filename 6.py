def find_zero(zero):
    p = 0
    while(zero>0):
        zero /= 2
        p += 1
    return p+1

def find_inf(inf):
    p = 0
    while(inf > 0):
        inf *= 2;
        p += 1
    return p

def find_eps(eps):
    prev_eps = eps
    k = 0
    while(eps+1 > 1):
        prev_eps = eps
        eps /= 2
        k += 1
    return prev_eps

