# RSA
RSA 加密演算法：
 1. 給定兩不相等質數 p, q
 2. 計算```N = p*q, phi(N) = (p-1)*(q-1)```
 3. 選擇 ```e```, 使得 ```gcd(phi(N), e) = 1, 1 < e < phi(N)```
 4. 計算 ```d = e^(-1) (mod phi(N))```
 加解密：```text = M，M < N```
 * encryption: ```C = M^e mode N```
 * decryption: ```M = C^d mode N```

## Solve
詳見[solve.py](solve.py)
  * ```Congratulations on decrypting an RSA message! Your flag is modular_arithmetics_not_so_bad_after_all```
