def invert_in_Zp_Euclead(a,b):
    if a == 0 or b == 0:
        return 0
    if a < b:
        a, b = b, a
    p = a
    j1, j2 = 1, 0
    x1, x2 = 0, 1
    
    while True:
        new_b = a % b
        if new_b == 0:
            break
        integer_division = a // b
        # new j1 and j2
        new_j2 = j1 - j2 * integer_division 
        j1 = j2
        j2 = new_j2
        # new x1 and x2
        new_x2 = x1 - x2 * integer_division
        x1 = x2
        x2 = new_x2
        # new a and b
        a = b
        b = new_b
        
    if b == 1:
        if x2 < 0:
            x2 = p + x2
        return x2
    else:
        return 0

def gcd(p, x):
    if(x == 0):
        return p
    else:
        return gcd(x, p % x)
     
def fast_pow_mod(x, y, m):
    if (y == 0):
        return 1
    p = fast_pow_mod(x, y // 2, m) % m
    p = (p * p) % m
  
    return p if(y % 2 == 0) else  (x * p) % m
 

def invert_in_Zp_Ferma(p, x):
    if p == 0 or x == 0:
        return 0
    if (gcd(p, x) != 1):
        return 0
    else:
        return fast_pow_mod(x, p - 2, p)