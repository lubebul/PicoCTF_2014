# ZOR
 * 看到[程式碼](ZOR.py)加密用的function：
```python
key ^= ((2 * ord(ch) + 3) & 0xff)
```
  * 和0xff做mask，所以key的範圍縮小到(0~255)
 * 只要暴力試出key是多少就解開了

## Solve
 * 在[ZOR.py](ZOR.py)中加入一個function：
```python
def solve(input_data):
    result = ""
    for key in range(256):
        result += xor(input_data, key) + "\n\n"
    return result
```
 * 成功取得flag
```
This message is for Daedalus Corporation only. Our blueprints for the Cyborg are protected with a password. That password is f6ddc997f218c7ddcc80f7172d938d
```
