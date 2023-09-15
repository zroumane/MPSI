print("E1")

print("E2")

def palindrome(s):
    r = True
    for i in range(round(len(s)/2)):
        if s[i] != s[len(s) - 1 -i]:
            r = False
    return r

print(palindrome('1234321'), palindrome('abcdefg'))


print("E3")

def retire_espaces(s):
    r = ""
    for i in range(len(s)):
        if s[i].isalpha():
            r += s[i]
    return r

print(retire_espaces('bonjour ca va'))

print("E4")

def palindrome_bis(s):
    return palindrome(retire_espaces(s))

print(palindrome_bis("a man, a plan, a canal : panama"))


print("E5")

def coincide(extrait, texte, i):
    r = True
    for n in range(len(extrait)):
        if n + i + 1 > len(texte):
            r = False
        elif texte[n + i] != extrait[n]:
            r = False
    return r

texte = "abracadabra"
print(coincide("brac", texte, 1))
print(coincide("brac", texte, 4))
print(coincide("brac", texte, 8))

print("E6")

def rechercher(extrait, texte):
    s = []
    for i in range(len(texte)):
        if texte[i] == extrait[0]:
            m = True
            for n in range(len(extrait)):
                if n + i + 1 > len(texte):
                    m = False
                elif texte[i + n] != extrait[n]:
                    m = False
            if m:
                s.append(i)
    return s

print(rechercher("abr", texte))


print("E7")

def q1(s):
    l1 = s[0]
    l2 = ".." + s[1]
    l3 = "...." + s[2]
    for i in range(3, len(s)):
        if i % 4 == 0:
            l1 += "......." + s[i]
        elif i % 2 == 1:
            l2 += "..." + s[i]
        elif i % 2 == 0:
            l3 += "......." + s[i]
    return l1 + "\n" + l2 + "\n" + l3


print(q1("Bonjour Python"))


def q2(s):
    l1 = s[0]
    l2 = s[1]
    l3 = s[2]
    for i in range(3, len(s)):
        if i % 4 == 0:
            l1 += s[i]
        elif i % 2 == 1:
            l2 += s[i]
        elif i % 2 == 0:
            l3 += s[i]
    return l1 + l2 + l3


print(q2("Bonjour Python"))


def q3(s):
    l2 = round(len(s) / 2)
    l1 = round(l2 / 2)
    r = ""
    for i in range(len(s)):
        if i % 4 == 0:
            r += s[i//4]
        elif i % 2 == 1:
            r += s[l1 + i//2]
        elif i % 2 == 0:
            r += s[l1 + l2 + i//4]
    return r


print(q3("v zmsosae opiuvc"))





