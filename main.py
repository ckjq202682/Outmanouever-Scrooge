a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
h = 'h'
i = 'i'
j = 'j'
k = 'k'
l = 'l'
m = 'm'
n = 'n'
o = 'o'
p = 'p'
q = 'q'
r = 'r'
s = 's'
t = 't'
u = 'u'
v = 'v'
w = 'w'
x = 'x'
y = 'y'
z = 'z'
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
H = 'H'
I = 'I'
J = 'J'
K = 'K'
L = 'L'
M = 'M'
N = 'N'
O = 'O'
P = 'P'
Q = 'Q'
R = 'R'
S = 'S'
T = 'T'
U = 'U'
V = 'V'
W = 'W'
X = 'X'
Y = 'Y'
Z = 'Z'
lowercase = [a,
             b,
             c,
             d,
             e,
             f,
             g,
             h,
             i,
             j,
             k,
             l,
             m,
             n,
             o,
             p,
             q,
             r,
             s,
             t,
             u,
             v,
             w,
             x,
             y,
             z]
capital = [A,
           B,
           C,
           D,
           E,
           F,
           G,
           H,
           I,
           J,
           K,
           L,
           M,
           N,
           O,
           P,
           Q,
           R,
           S,
           T,
           U,
           V,
           W,
           X,
           Y,
           Z]
def findB(capital):
    place = 0
    if 'B' in capital:
        place = capital.index('B')
    return place
def finda(lowercase):
    place = 0
    if 'a' in lowercase:
        place = lowercase.index('a')
    return place
def findh(lowercase):
    place = 0
    if 'h' in lowercase:
        place = lowercase.index('h')
    return place
def findH(capital):
    place = 0
    if 'H' in capital:
        place = capital.index('H')
    return place
def findu(lowercase):
    place = 0
    if 'u' in lowercase:
        place = lowercase.index('u')
    return place
def findm(lowercase):
    place = 0
    if 'm' in lowercase:
        place = lowercase.index('m')
    return place
def findb(lowercase):
    place = 0
    if 'b' in lowercase:
        place = lowercase.index('b')
    return place
def findg(lowercase):
    place = 0
    if 'g' in lowercase:
        place = lowercase.index('g')
    return place
def check(bah, humbug):
    string = bah + ' ' + humbug
    if string == "Bah Humbug":
        return True
    else:
        return False
valid = False
while valid == False:
    letter1 = capital[findB(capital)]
    letter2 = lowercase[finda(lowercase)]
    letter3 = lowercase[findh(lowercase)]
    letter4 = capital[findH(capital)]
    letter5 = lowercase[findu(lowercase)]
    letter6 = lowercase[findm(lowercase)]
    letter7 = lowercase[findb(lowercase)]
    letter8 = lowercase[findu(lowercase)]
    letter9 = lowercase[findg(lowercase)]
    bah = letter1 + letter2 + letter3
    humbug = letter4 + letter5 + letter6 + letter7 + letter8 + letter9
    valid = check(bah, humbug)
print(bah, ' ', humbug)