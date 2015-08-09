# Netsino
[netsino.c](netsino.c) 在讀數字用的`getnum()`
 * `num`型別是`uint64_t`，可回傳的卻是`long`
  * `long`: 在不同機器上，有可能只介於+-(2^31-1)之間，實際測試確實是`[-2^31+1, 2^31-1]`
  * `LONG_MAX` >= `2^31-1`，實際測試後，發現`LONG_MAX = 2^32-1`
   * `bet = (1 << 32)`，時，顯示會得到的金額皆為0，因為剛好overflow了！
```
$ python solve.py
Arr, git ye into me casio, the hottest gamblin' sensation on the net!
Here, take twenty, and let's gamble!
You've got $20. How much you wanna bet on this next toss?
> 4294967296
4294967296
1: EVEN. Win your bet back plus an additional $0 if the dice sum even.
2: ODDS. Win your bet back plus an additional $0 if both dice roll odd.
3: HIGH. Win your bet back plus an additional $0 if the dice sum to 10 or more.
4: FOUR. Win your bet back plus an additional $0 if the dice sum to four.
5: EYES. Win your bet back plus an additional $0 on snake eyes.
```
 * `getbet()`：只要overflow變成<=0，就可以跳過對玩家現金的檢查
 * 在overflow的情況下，如果賭輸了 => **boss會扣錢，而玩家現金會增加**
 * 所以，只要overflow成夠大的負數，就能夠快速取得flag！

## Solve
我使用[pexpect](https://pexpect.readthedocs.org)，自動和server 互動
 * 詳見 [solve.py](solve.py)
```
$ python solve.py
Arr, git ye into me casio, the hottest gamblin' sensation on the net!
Fifty bucks says you'll lose it back to me!
You've got $50. How much you wanna bet on this next toss?
> 2147483648
2147483648
1: EVEN. Win your bet back plus an additional $2147483648 if the dice sum even.
2: ODDS. Win your bet back plus an additional $2147483648 if both dice roll odd.
3: HIGH. Win your bet back plus an additional $2147483648 if the dice sum to 10 or more.
4: FOUR. Win your bet back plus an additional $0 if the dice sum to four.
5: EYES. Win your bet back plus an additional $2147483648 on snake eyes.
What'll it be?
> 5
5
Lets rock 'n' roll!
5 3
Snake eyes! ...not.
Great, I'm fresh outta cash. Take this flag instead.
i_wish_real_casinos_had_this_bug
Git outta here.
flag = ['i_wish_real_casinos_had_this_bug']
```
