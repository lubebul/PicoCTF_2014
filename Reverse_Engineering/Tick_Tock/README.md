# Tick Tock
仔細看程式碼，會發現這是個數學題：
 1. 求一個整數num，使得對於所有secretz中的(m, r)，num % m == r
   * 用中國餘式定理求解：
    * let num = 0, n = 所有m的乘積
    * 對每個m, 找出 x，使得 ```r == x*(n/m)，num += x * (n/m)```
 2. 求整數num2，使得 ```(num ** num2) % 200009*160009 == 1```
   * 使用Euler's totient function theory:  <img src="euler's theory.png">
   * 因為200009和160009都是質數，所以 num2 = ```phi(200009*160009) = (200009-1)*(160009-1)```

```
$ python solve.py
Congratulations! The flag is: 930969879919543277249858199448477560510863616444995705_32002880064
```
