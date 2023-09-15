print("\nEX 1")

#a = [[[3,2,1], [4,8,2]], [[7,-1,3], [8,-2,9]], [[0,0,4],[6,-7,5]], [[3,-3,2], [4,1,8]]]

#print(a[2])
#print(a[2][0])
#print(a[2][0][1])
#print(a[1][1])
#print(a[3])
#print(a[0][1][2])


print("\nEX 2")

def diag(n):
	L = []
	d = 0
	for i in range(n):
		L.append([1 if i == d else 0 for i in range(n)])
		d+=1
	return L


#print(diag(4))


print("\nEX 3")

import matplotlib.pyplot as plt

m=[[[0,0,0],[0.4,0.4,0.4]],[[0,0,1],[1,1,0]]]

def france():
	P = []
	for i in range(90):
		P.append([])
		for j in range(135):
			a = []
			if j <= 45:
				a = [0.0,0.0,1.0]
			elif j >= 90:
				a = [1.0,0.0,0.0]
			else:
				a = [1.0,1.0,1.0]
			P[i].append(a)
	return P

def allemagne():
	P = []
	for i in range(90):
		P.append([])
		for j in range(135):
			a = []
			if i <= 30:
				a = [0.0,0.0,0.0]
			elif i >= 60:
				a = [1.0,1.0,0.0]
			else:
				a = [1.0,0.0,0.0]
			P[i].append(a)
	return P


def finlande():
	P = []
	for i in range(90):
		P.append([])
		for j in range(135):
			a = []
			if (i > 38 and i < 52) or (j > 38 and j < 52):
				a = [0.0,0.0,1.0]
			else:
				a = [1.0,1.0,1.0]
			P[i].append(a)
	return P


def suisse():
	P = []
	for i in range(90):
		P.append([])
		for j in range(135):
			a = []
			if (j > 60 and j < 74 and i > 25 and i < 65) or (i > 38 and i < 52 and j > 47 and j < 87):
				a = [1.0,1.0,1.0]
			else:
				a = [1.0,0.0,0.0]
			P[i].append(a)
	return P


I = plt.imread("F:\TP inp\Image_created_with_a_mobile_phone.png")

def miroir(a):
	return [[a[r][len(a[r]) - c - 1] for c in range(len(a[r]))] for r in range(len(a))]

def rotation90(a):
	return [[a[r][len(a[r]) - c - 1] for r in range(len(a))] for c in range(len(a[0]))]
	
def gris(a):
	L = a.copy()
	for r in range(len(a)):
		for c in range(len(a[r])):
			L[r][c] = [(a[r][c][0] + a[r][c][1] + a[r][c][2])/ 3] * 3 + [1]
	return L

def floutage(a, n):
	L = a.copy()
	for k in range(3): # chaque luminance
		for r in range(1, len(a) - 1): # chaque ligne
			for c in range(1, len(a[r]) - 1): # chaque colone
				m = 0 # moyenne
				for i in range(3):
					for j in range(3):
						m += a[r+i-1][c+j-1][k]
				L[r][c][k] = m / 9
	
	return L if n == 0 else floutage(L, n-1)

def japon():
	P = []
	for i in range(90):
		P.append([])
		for j in range(135):
			P[i].append([1.0, 0.0, 0.0] if (i - 45)**2 + (j - 67)**2 < 25**2 else [1.0, 1.0, 1.0])
	return P


# plt.imshow(m, interpolation="none")
# plt.imshow(france(), interpolation="none")
# plt.imshow(allemagne(), interpolation="none")
# plt.imshow(finlande(), interpolation="none")
# plt.imshow(suisse(), interpolation="none")
# plt.imshow(miroir(I), interpolation="none")
# plt.imshow(rotation90(I), interpolation="none")
# plt.imshow(gris(I), interpolation="none")
plt.imshow(floutage(I, 20), interpolation="none")
# plt.imshow(japon(), interpolation="none")

plt.show()







