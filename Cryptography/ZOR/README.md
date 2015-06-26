# ZOR
給你一段加解密的python程式碼，flag藏在原文中
 * 看到程式碼加密用的function：
```python
key ^= ((2 * ord(ch) + 3) & 0xff)
```
  * 和0xff做mask，所以key的範圍縮小到(0,255)之間，那麼只要暴力試出key是多少就解開了。
 * 我寫了一個function來解：
```python
def solve(input_data):
    result = ""
    for key in range(0,255):
        result += xor(input_data, key) + "\n\n"
    return result
```
 * 然後看output結果，成功取得flag。
```
This message is for Daedalus Corporation only. Our blueprints for the Cyborg are protected with a password. That password is f6ddc997f218c7ddcc80f7172d938d
```
