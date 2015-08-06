# Supercow
在`/home/daedalus/supercow`目錄下，有一支會印`*.cow`內容的程式，說不定我們可以拿它來看flag.txt
 * 把`flag.txt` 更名成`flag.cow`
  * 有權限問題，flag.txt無法直接更名
  * [題目給的參考資料](https://en.wikipedia.org/wiki/Symbolic_link)，提供了解決方法
  * 創一個叫作flag.cow的symbolic link指到flag.txt就行了

```
$ ln -s flag.txt flag.cow
ln: failed to create symbolic link 'flag.cow': Permission denied
$ ln -s /home/daedalus/flag.txt /home_users/pico62895/flag.cow
$ ./supercow /home_users/pico62895/flag.cow
 ___________________________
< cows_drive_mooooving_vans >
 ---------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
