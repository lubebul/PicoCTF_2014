# Bit Puzzle 
 * 使用objdump來看[bitpuzzle](bitpuzzle)的assembly code
```
$ objdump -d bitpuzzle
...
8048502:	8d 5c 24 1c          	lea    0x1c(%esp),%ebx
...
8048527:	a1 24 a0 04 08       	mov    0x804a024,%eax
804852c:	89 44 24 08          	mov    %eax,0x8(%esp)
8048530:	c7 44 24 04 50 00 00 	movl   $0x50,0x4(%esp)
8048538:	89 1c 24             	mov    %ebx,(%esp)
804853b:	e8 90 fe ff ff       	call   80483d0 <fgets@plt>
```
 * ```char *fgets(char *s, int size, FILE *stream)```
  * 把argument放到stack上的順序是**相反的**
  * ```mov    0x804a024,%eax; mov    %eax,0x8(%esp)``` -> stream
  * ```movl   $0x50,0x4(%esp)``` -> size
  * ```lea    0x1c(%esp),%ebx; mov    %ebx,(%esp)``` -> s
 * 得知size = 80 byte，繼續看下去程式對input做了什麼：
```
8048540:	ba ff ff ff ff       	mov    $0xffffffff,%edx
8048545:	89 df                	mov    %ebx,%edi; s -> edi
8048547:	b8 00 00 00 00       	mov    $0x0,%eax
804854c:	89 d1                	mov    %edx,%ecx; %ecx = 0xffffffff
804854e:	f2 ae                	repnz scas %es:(%edi),%al; => %ecx = 0xffffffff - len(s)
8048550:	f7 d1                	not    %ecx ; %ecx = len(s)
8048552:	c6 44 0c 1a 00       	movb   $0x0,0x1a(%esp,%ecx,1); s[%ecx] = 0
```
  * scas(scan string): 比較在al(=0) 和 es:edi的byte，如果相同就把status flag設1，不相同**decrement %ecx**
  * repnz：只要scas的status flag不相同就重複
  * 所以離開repnz，```%ecx = 0xffffffff - len(s)```
  * s 在```0x1C(%esp)```，所以```0x1A+%ecx+%esp```會指到len(s)
  * 可以看出這是常用的```s[len(s)] = 0```
 * 繼續看下去：
```
8048557:	89 df                	mov    %ebx,%edi; s -> %edi
8048559:	89 d1                	mov    %edx,%ecx
804855b:	f2 ae                	repnz scas %es:(%edi),%al; %ecx = len(s)
804855d:	83 f9 de             	cmp    $0xffffffde,%ecx
```
  * ```cmp    $0xffffffde,%ecx```：如果```len(s) = 0x00000021```，就會compare成功
   * equal：```je     8048582 <__libc_start_main@plt+0x162>```，跳到```.text:8048582```
   * not equeal：印失敗訊息並呼叫exit
```
   8048562:	8d 44 24 1c          	lea    0x1c(%esp),%eax
   8048566:	89 44 24 04          	mov    %eax,0x4(%esp)
   804856a:	c7 04 24 f0 87 04 08 	movl   $0x80487f0,(%esp)
   8048571:	e8 4a fe ff ff       	call   80483c0 <printf@plt>
   8048576:	c7 04 24 00 00 00 00 	movl   $0x0,(%esp)
   804857d:	e8 8e fe ff ff       	call   8048410 <exit@plt>
```
 * 可以知道len(input string)必須 = 33 byte
```
 8048582:	8b 54 24 1c          	mov    0x1c(%esp),%edx; %edx = s[0:4]
 8048586:	8b 44 24 20          	mov    0x20(%esp),%eax; %eax = s[4:8]
 804858a:	8b 7c 24 24          	mov    0x24(%esp),%edi; %edi = s[8:12]
 804858e:	8d 1c 07             	lea    (%edi,%eax,1),%ebx; %ebx = s[4:8] + s[8:12]
 ...
 8048596:	81 fb ce df dc c0    	cmp    $0xc0dcdfce,%ebx; s[4:8] + s[8:12] == 0xc0dcdfce?
 804859c:	75 0f                	jne    80485ad <__libc_start_main@plt+0x18d>
 804859e:	8d 0c 10             	lea    (%eax,%edx,1),%ecx; %ecx = s[0:4] + s[4:8]
 80485a1:	81 f9 dc dd d3 d5    	cmp    $0xd5d3dddc,%ecx; s[0:4] + s[4:8] == 0xd5d3dddc?
 ...
 80485ad:	8d 34 52             	lea    (%edx,%edx,2),%esi; %esi = s[0:4] + s[0:4]*2
 80485b0:	8d 1c 80             	lea    (%eax,%eax,4),%ebx; %ebx = s[4:8] + s[4:8]*4
 80485b3:	8d 1c 33             	lea    (%ebx,%esi,1),%ebx; %ebx =  s[4:8] + s[4:8]*4 + s[0:4] + s[0:4]*2
 80485b6:	81 fb 66 76 4a 40    	cmp    $0x404a7666,%ebx;  s[4:8]*5 + s[0:4]*3 == 0x404a7666?
 ...
 80485c4:	8b 5c 24 28          	mov    0x28(%esp),%ebx
 80485c8:	31 d3                	xor    %edx,%ebx
 80485ca:	81 fb 07 06 03 18    	cmp    $0x18030607,%ebx; s[0:4] ^ s[12:16] == 0x18030607?
 ...
 80485d8:	23 54 24 28          	and    0x28(%esp),%edx
 80485dc:	81 fa 70 69 6c 66    	cmp    $0x666c6970,%edx; s[0:4] & s[12:16] == 0x666c6970?
 ...
 80485ea:	8b 5c 24 2c          	mov    0x2c(%esp),%ebx
 80485ee:	0f af c3             	imul   %ebx,%eax
 80485f1:	3d 2b 90 80 b1       	cmp    $0xb180902b,%eax; s[4:8] * s[16:20] == 0xb180902b?
...
 80485fe:	89 d8                	mov    %ebx,%eax; %eax = s[16:20]
 8048600:	0f af c7             	imul   %edi,%eax
 8048603:	3d 5f 6b 43 3e       	cmp    $0x3e436b5f,%eax; s[16:20] * s[8:12] == 0x3e436b5f?
...
 8048610:	8b 74 24 30          	mov    0x30(%esp),%esi; %esi = s[20:24]
 8048614:	8d 04 73             	lea    (%ebx,%esi,2),%eax
 8048617:	3d 31 38 48 5c       	cmp    $0x5c483831,%eax; s[16:20] + s[20:24]*2 == 0x5c483831?
 ...
 8048624:	89 f0                	mov    %esi,%eax; %eax = s[20:24]
 8048626:	25 00 00 00 70       	and    $0x70000000,%eax
 804862b:	3d 00 00 00 70       	cmp    $0x70000000,%eax; s[20:24] & 0x70000000 == 0x70000000?
 ...
 8048638:	89 f0                	mov    %esi,%eax
 804863a:	ba 00 00 00 00       	mov    $0x0,%edx
 804863f:	f7 74 24 34          	divl   0x34(%esp)
 8048643:	83 f8 01             	cmp    $0x1,%eax; s[20:24]/s[24:28] == 0x1?
...
 804864e:	89 f0                	mov    %esi,%eax
 8048650:	ba 00 00 00 00       	mov    $0x0,%edx
 8048655:	f7 74 24 34          	divl   0x34(%esp)
 8048659:	81 fa ec 0c 00 0e    	cmp    $0xe000cec,%edx; s[20:24] % s[24:28] == 0xe000cec?
...
 8048667:	8b 44 24 38          	mov    0x38(%esp),%eax; %eax = s[28:32]
 804866b:	8d 14 5b             	lea    (%ebx,%ebx,2),%edx
 804866e:	8d 14 42             	lea    (%edx,%eax,2),%edx
 8048671:	81 fa 17 eb 26 37    	cmp    $0x3726eb17,%edx; s[16:20]*3 + s[28:32]*2 == 0x3726eb17?
...
 804867f:	8d 14 c5 00 00 00 00 	lea    0x0(,%eax,8),%edx
 8048686:	29 c2                	sub    %eax,%edx
 8048688:	8d 14 ba             	lea    (%edx,%edi,4),%edx
 804868b:	81 fa 2d 92 0b 8b    	cmp    $0x8b0b922d,%edx; s[28:32]*7 + s[8:12]*4 == 0x8b0b922d?
...
 8048699:	8d 04 40             	lea    (%eax,%eax,2),%eax
 804869c:	03 44 24 28          	add    0x28(%esp),%eax
 80486a0:	3d 91 9c cf b9       	cmp    $0xb9cf9c91,%eax; s[28:32]*3 + s[12:16] == 0xb9cf9c91?
```
 * 會發現一系列的比較：
  1. ```s[4:8] + s[8:12] == 0xc0dcdfce```?
  2. ```s[0:4] + s[4:8] == 0xd5d3dddc```?
  3. ```s[4:8]*5 + s[0:4]*3 == 0x404a7666```?
  4. ```s[0:4] ^ s[12:16] == 0x18030607```?
  5. ```s[0:4] & s[12:16] == 0x666c6970```?
  6. ```s[4:8] * s[16:20] == 0xb180902b```?
  7. ```s[16:20] * s[8:12] == 0x3e436b5f```?
  8. ```s[16:20] + s[20:24]*2 == 0x5c483831```?
  9. ```s[20:24] & 0x70000000 == 0x70000000```?
  10. ```s[20:24]/s[24:28] == 0x1```?
  11. ```s[20:24] % s[24:28] == 0xe000cec```?
  12. ```s[16:20]*3 + s[28:32]*2 == 0x3726eb17```?
  13. ```s[28:32]*7 + s[8:12]*4 == 0x8b0b922d```?
  14. ```s[28:32]*3 + s[12:16] == 0xb9cf9c91```?
 * 如果直接暴力解組合太多，從constrain 9.10.11.下手：
  * s[20:24] & 0x70000000 == 0x70000000
  * s[20:24] = s[24:28] + 0xe000cec
 * 寫個[程式](solve.c)解：
```
$ gcc solve.c -o solve
$ ./solve
solving_equations_is_lots_of_fun
```
