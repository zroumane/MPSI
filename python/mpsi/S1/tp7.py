file = "Q:\\Documents en consultation\\nombres.txt"
f=open(file, mode="r", encoding="latin1")
nb=len(f.readlines())
n7=0
f=open(file, encoding="latin1")
for i in range(nb):
    s = f.readline()
    if int(s) % 7 == 0 :
        n7 += 1

print("il y a "+str(nb)+" nombres dont "+str(n7)+" divisible par 7")

f=open("F:\\TP inp\\nombres.txt", mode="w", encoding="latin1")
for n in range(10000):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime:
        f.write(str(n) + "\n")
f.close()