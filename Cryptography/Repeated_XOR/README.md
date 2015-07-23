# Repeated XOR
拿到一個hex encoded的密文encrypt.txt，只知道是由XOR key加密的，key長度未知。

## 解題思路
 1. 固定長度的key，同一位加密同個字母會得到同樣的答案
  * 計算兩個重複字母的差，key的長度一定會是這些差的最大公因數的因數
 2. 猜出key長度後，就能對key的每一位當作single XOR各自擊破
  * 測試所有可能ascii碼，key的這一位，就是能產生最多英文正常用字的那個

寫了個小程式：solve.py

解得： your flag is: 29a70d3fe359728436dde20c004879692776be22
