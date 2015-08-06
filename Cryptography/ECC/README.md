# ECC
Cryptosystem:
 * Elliptic Curve: `y^2 ≡ x^3 + ax + b mod n`
  * a = 0, n = 928669833265826932708591
  * 求b = ?
 * Decryption: M = d * C mod n
  * d = 87441340171043308346177, C = (236857987845294655469221, 12418605208975891779391)
  * 求M = ?

## Solve
 1. 安裝 sage：可能要花好幾小時..
 2. 解b = 268892790095131465246420
 3. 使用sage建出橢圓曲線
  ```EllipticCurve(GF(n), [0,0,0,0,b])```
 4. 解Ｍ = d*E.point(C)

印出STR(M[0]), STR(M[1]):

```
 $ sage solve.py
E
L
L
I
P
T
I
C

C
U
R
V
E
S

A
R
E

F
U
N
```
詳見[solve.py](solve.py)
