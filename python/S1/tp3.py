print("EX 1")

import math

print(math.pi, math.e)



print("EX 2")
print(math.cos(math.pi/3))


print("EX 3")

def trigo(n):
    L = []
    for i in range(n):
        L.append(math.sin(i*2*math.pi/n))
    return L
    
print(trigo(5))


print("EX 4")

import matplotlib.pyplot as plt

print("EX 5")

#plt.plot([1,4,2,3],[3,0,1,2])
#plt.show()


print("EX 6")

plt.plot([1,1,2,3,3],[1,2,1.5,2,1])
plt.plot([4,4,6,6,4],[1,2,2,1.5,1.5])
plt.plot([7,9,9,7,7,9],[1,1,1.5,1.5,2,2])
plt.plot([10,12,11,11,10,12],[1,1,1,2,2,2])
plt.xlim(0, 13)
plt.ylim(0.5, 2.5)
plt.show()


print("EX 7")

plt.plot([1,4,2,3,2],[3,0,1,2])
plt.show()


print("EX 8")

X=[]
Y=[]
for i in range(100):
    X.append(math.cos(i*2*math.pi/100))
    Y.append(math.sin(i*2*math.pi/100))
    
plt.plot(X, Y)
plt.show()


print("EX 9")

plt.plot([i/10 for i in range(100)], [math.sin(i/10) for i in range(100)])

print("EX 10")

def f(x):
    return math.sin(x)

def images(L, f):
    return [f(x) for x in L]

def abscisses(a, b, N):
    return [a+i*(b-a)/(N) for i in range(N+1)]

def tracer(f, a, b, N):
    x = abscisses(-10, 10, 100)
    y = images(x, f)
    plt.plot(x, y)    
    
tracer(f, -10, 10, 100)








































