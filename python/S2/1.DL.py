# Helpers
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def check(a):
	return [(0, 1) if i[0] == 0 else symplify(int(i[0]), int(i[1])) for i in a]

def truncate(a, n):
    return a[:(n+1)]

# Question 1
def pgcd(n,p):
    a=n
    b=p
    while b!=0:
        q,r = divmod(a,b)
        a=b
        b=r
    return a

# Question 2 : 0 -> 0 / 1 ; n -> n / 1

# Question 3
def symplify(num, den):
    a = pgcd(num, den)
    while a != 1:
        num //= a
        den //= a
        a = pgcd(num, den)
    return num, den

# Question 4
assert(symplify(60, -75) == (-4, 5))

# Question 5
def r_add(q,r):
    return symplify(q[0]*r[1] + q[1]*r[0], q[1]*r[1])

def r_mul(q,r):
    return symplify(q[0]*r[0], q[1]*r[1])

# Question 6
assert(r_add((3,2), (1,3)) == (11, 6))
assert(r_mul((3,2), (1,3)) == (1, 2))

# Question 7
def dl_const(r, n):
    return [r] + [(0,1) for i in range(1, n+1)]

# Question 8
def cos(n):
    return [((-1)**(i//2), fact(i)) if i % 2 == 0 else (0, 1) for i in range(0, n+1)]

# Question 8
assert(cos(4) == [(1, 1), (0, 1), (-1, 2), (0, 1), (1, 24)])

# Question 10
def dl_prim(a):
    return check([(0,1)] + [(a[i][0], a[i][1]*(i+1)) for i in range(len(a)-1)])

# Question 11
assert(dl_prim(cos(3)) == [(0, 1), (1, 1), (0, 1), (-1, 6)])

# Question 12
def sin(n):
    return dl_prim(cos(n))

# Question 13
def dl_add(a, b):
    return check([(r_add(a[i], b[i])) for i in range(len(a) if len(a) < len(b) else len(b))])

assert(dl_add([(1,3),(2,5)], [(3,2), (1, 10)]) == [(11, 6), (1, 2)])

# Question 14
def dl_mul_simple(a, r, k):
    L = []
    for i in range(len(a) + k):
        if i < k:
            L.append((0, 1))
        else:
            L.append(r_mul(a[i-k], r))
    return check(L)

def dl_mul(a, b):
    L = []
    m = len(a) if len(a) > len(b) else len(b)
    for i in range(len(a)):
        L.append(truncate(dl_mul_simple(b, a[i], i), m))
    G = [(0, 1)] * m
    for i in L:
        i += [(0, 1)] * (m - len(i))
        G = dl_add(G, i)
    return check(G)

# Question 15
assert(dl_add(dl_mul(cos(3), cos(3)), dl_mul(sin(3), sin(3))) == dl_const((1,1), 3))

# Question 16
def dl_pow(a, k):
    L = a.copy()
    if k == 0:
        return [(1,1)] + [(0,1)] * (len(a))
    for _ in range(k - 1):
        L = truncate(dl_mul(L, a), len(a))
    return check(L)

assert(dl_pow(cos(4), 2) == [(1, 1), (0, 1), (-1, 1), (0, 1), (1, 3)])

# Question 17
def dl_compo(a,b):
    L = []
    m = len(a)
    for i in range(m):
        v = truncate(dl_pow(b, i), m)
        L.append(truncate(dl_mul_simple(v, a[i], 0), m))
    G = [(0, 1)] * m
    for i in L:
        i += [(0, 1)] * (m - len(i))
        G = dl_add(G, i)
    return check(G)

# Question 18
def usumux(n):
    return [(1,1)]*(n + 1)

# Question 19
def dl_moinsx(n):
    return [(0, 1), (-1, 1)] + [(0, 1)]*(n-1)

def dl_moinsx2(n):
    return [(0, 1), (0, 1), (-1, 1)] + [(0, 1)]*(n-2)

def usupux(n):
    return dl_compo(usumux(n), dl_moinsx(n))

def usupux2(n):
    return dl_compo(usumux(n), dl_moinsx2(n))

def dl_ln(n):
    return dl_prim(usupux(n))

def dl_atan(n):
    return dl_prim(usupux2(n))


# Question 20
def exp(n):
    return check([(1,1)] + [(1, fact(i)) for i in range(1, n + 1)])

def upxa(a, n):
    return dl_compo(exp(n), dl_mul(dl_const(a, n), dl_ln(n)))

# Question 21
def int_exp(n):
    s = ''
    for i in str(abs(n)):
        s += ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸'][int(i)]
    return s

# Question 22
def int_ind(n):
    s = ''
    for i in str(abs(n)):
        s += ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈'][int(i)]
    return s

# Question 22
def pretty_dl(a):
    s = ''
    for i in range(len(a)):
        if a[i][0] == 0:
            continue
        if s != '':
            s +=' - ' if a[i][0] / a[i][1] < 0 else ' + '
        if a[i][1] == 1:
            s += str(a[i][0]) if a[i][0] != 1 else ''
        else:
            s += int_exp(a[i][0]) + '/' + int_ind(a[i][1])
        s += 'x' + (int_exp(i) if i != 1 else '') if i != 0 else ''
    return s + f' + ο(x{int_exp(len(a) - 1)})'


print(pretty_dl(exp(6)))
