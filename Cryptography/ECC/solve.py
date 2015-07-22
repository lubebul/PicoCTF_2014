from sage.all import *


def STR(a):
    a = str(a)
    for i in range(0, len(a)-1, 2):
        print chr(int(a[i:i+2]))


def solve_b(x, y, n):
    y_left = (y*y) % n
    x_left = (x**3) % n
    return y_left-x_left if y_left > x_left else y_left+n-x_left


e, d = 141597355687225811174313, 87441340171043308346177
n = 928669833265826932708591
C = (236857987845294655469221, 12418605208975891779391)
b = solve_b(C[0], C[1], n)
E = EllipticCurve(GF(n), [0, 0, 0, 0, b])
M = d*E.point(C)

print STR(M[0]) + STR(M[1])
