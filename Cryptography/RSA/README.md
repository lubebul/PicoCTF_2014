# RSA
RSA 加密演算法：
 1. 給定兩不相等質數 p, q
 2. 計算N = p*q, phi(N) = (p-1)*(q-1)
 3. 選擇 e, st gcd(phi(N), e) = 1, 1 < e < phi(N)
 4. 計算 d = e^(-1) (mod phi(N))
 加解密：text = M，M < N
 * encryption: C = M^e mode N
 * decryption: M = C^d mode N

得到 Congratulations on decrypting an RSA message! Your flag is modular_arithmetics_not_so_bad_after_all
