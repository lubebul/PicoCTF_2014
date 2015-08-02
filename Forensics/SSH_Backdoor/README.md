# SSH Backdoor
提示：hacker留了後門，也許你可以拿來和openssh原始碼做比較？
 * 下載[openssh-6.7](openssh-6.7p1_origin.zip)，並使用 diff 察看hacker改了什麼檔案：
```
$ diff openssh-6.7p1_pico openssh-6.7p1_origin/
diff openssh-6.7p1_pico/auth.c openssh-6.7p1_origin/auth.c
777,794d776
<
< static int frobcmp(const char *chk, const char *str) {
< 	int rc = 0;
< 	size_t len = strlen(str);
< 	char *s = xstrdup(str);
< 	memfrob(s, len);
<
< 	if (strcmp(chk, s) == 0) {
< 		rc = 1;
< 	}
<
< 	free(s);
< 	return rc;
< }
<
< int check_password(const char *password) {
< 	return frobcmp("CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY", password);
< }
diff openssh-6.7p1_pico/auth.h openssh-6.7p1_origin/auth.h
214,215d213
< int check_password(const char *);
<
diff openssh-6.7p1_pico/auth-passwd.c openssh-6.7p1_origin/auth-passwd.c
115,117d114
< 	if (check_password(password)) {
< 		return ok;
< 	}
Only in openssh-6.7p1_pico: buildpkg.sh
Only in openssh-6.7p1_pico: config.h
Only in openssh-6.7p1_pico: config.log
Only in openssh-6.7p1_pico: config.status
Common subdirectories: openssh-6.7p1_pico/contrib and openssh-6.7p1_origin/contrib
Only in openssh-6.7p1_pico: Makefile
Common subdirectories: openssh-6.7p1_pico/openbsd-compat and openssh-6.7p1_origin/openbsd-compat
Only in openssh-6.7p1_pico: opensshd.init
Only in openssh-6.7p1_pico: openssh.xml
Common subdirectories: openssh-6.7p1_pico/regress and openssh-6.7p1_origin/regress
Common subdirectories: openssh-6.7p1_pico/scard and openssh-6.7p1_origin/scard
Only in openssh-6.7p1_pico: survey.sh
```
diff 告訴我們，hacker把authentication method 改成：
 * ```frobcmp("CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY", password)```檢查通過，就能登入server
  * frobcmp 把加密後的password 和```"CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY"```比較
  * 加密password的方法是：```memfrob(xstrdup(password), strlen(password))```
 * 看看 memfrob 做什麼：$ man memfrob
```
SYNOPSIS
       #define _GNU_SOURCE             /* See feature_test_macros(7) */
       #include <string.h>

       void *memfrob(void *s, size_t n);
DESCRIPTION
       The memfrob() function encrypts the first n bytes of the memory
       area s by exclusive-ORing each character with  the  number  42.
       The  effect can be reversed by using memfrob() on the encrypted
       memory area.

       Note that this function is not a proper encryption  routine  as
       the  XOR  constant  is  fixed,  and is suitable only for hiding
       strings.
```
 * 重點：**The  effect can be reversed by using memfrob() on the encrypted
 memory area.**
 * 所以，寫了一個[程式](gen_password.c)，對```"CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY"```做一次memfrob
  * 得到password = ```iminyourmachinestealingyourflags```
 * 拿去登入backdoor.picoctf.com：
```
$ ssh jon@backdoor.picoctf.com
jon@backdoor.picoctf.com's password:
Last login: Wed Jul 22 20:14:47 2015 from f053221121.adsl.alicedsl.de
jon@ip-10-45-162-116:~$ ls
flag.txt
jon@ip-10-45-162-116:~$ cat flag.txt
ssshhhhh_theres_a_backdoor
```
