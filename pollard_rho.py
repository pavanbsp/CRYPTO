def isqrt(n): # newton
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def isSquare(n):
    if 33751571>>(int(n)%32)&1==0: return False
    if 38348435>>(int(n)%27)&1==0: return False
    if 19483219>>(int(n)%25)&1==0: return False
    if   199411>>(int(n)%19)&1==0: return False
    if   107287>>(int(n)%17)&1==0: return False
    if     5659>>(int(n)%13)&1==0: return False
    if      571>>(int(n)%11)&1==0: return False 
    if       23>>(int(n)% 7)&1==0: return False
    s = isqrt(n)
    if s * s == n: return s
    return False

def isPrime(n, k=5): # miller-rabin
    from random import randint
    ps = [2,3,5,7,11,13,17,19,23,29]
    if n < 2: return False
    for p in ps:
        if n%p == 0: return n==p
    s, d = 0, n-1
    while d%2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

def factors(n):
    def gcd(a, b): # euclid
        if b == 0: return a
        return gcd(b, a%b)
    # 2,3,5-wheel to cube root of n
    wheel = [1,2,2,4,2,4,2,4,6,2,6]
    w, f = 0, 2
    d = dict()
    while f*f*f <= n:
        while n % f == 0:
            if f not in d:
                d[f] = 1
            else:
                d[f]+=1
            n //= f
        if n == 1: return d
        if isPrime(n):
            if n not in d:
                d[n] = 1
            else:
                d[n]+=1
            return d
        f, w = f+wheel[w], w+1
        if w == 11: w = 3

    if isSquare(n):
        f = isqrt(n)
        if f not in d:
            d[f] = 2
        else:
            d[f]+=2
        return d

    for i in range(1,n):
        s = isqrt(n*i)
        if s*s <= n*i: s += 1
        m = pow(s,2,n)
        if isSquare(m):
            t = isqrt(m)
            f = gcd(n, s-t)
            if f not in d:
                d[f] = 1
            else:
                d[f]+=1
            if n//f not in d:
                d[n//f] = 1
            else:   
                d[n//f]+=1
            return d
