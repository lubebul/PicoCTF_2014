# Towers of Toast
拿到一個遊戲原始碼，flag在破關時才會自動產生。只要看懂代碼就能hack拿到flag。
```java
// 加在new 後面
pole1.addAll(pole2);
pole1.addAll(pole3);
checkVictory(pole1, pole2, pole3);
```

```bash
$ java Main
Welcome to Towers of Toast!!!
Type 'new' to start a new random puzzle
Type 'load' to load a saved puzzle
new
[2, 3, 5, 7, 10, 14, 16, 17, 19, 21, 28, 35, 38]
[1, 9, 12, 13, 18, 23, 24, 29, 32, 34, 36, 37, 39]
[0, 4, 6, 8, 11, 15, 20, 22, 25, 26, 27, 30, 31, 33]
                   |                                       |
                   XX                                      X                                      XXXX
                  XXX                                  XXXXXXXXX                                 XXXXXX
                 XXXXX                                XXXXXXXXXXXX                              XXXXXXXX
                XXXXXXX                              XXXXXXXXXXXXX                            XXXXXXXXXXX
               XXXXXXXXXX                          XXXXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXX
             XXXXXXXXXXXXXX                     XXXXXXXXXXXXXXXXXXXXXXX                   XXXXXXXXXXXXXXXXXXXX
            XXXXXXXXXXXXXXXX                    XXXXXXXXXXXXXXXXXXXXXXXX                 XXXXXXXXXXXXXXXXXXXXXX
           XXXXXXXXXXXXXXXXX                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXX               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           XXXXXXXXXXXXXXXXXXXXXXXXXX
         XXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXXXXXXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Sorry the game is broken! :(
We saved your game, though. Here are your save game numbers:
698894708637563715095
905996974780249568207097
263093535682696765930994
YOU WIN!
Your flag is: 166589903787325219380851695350896256250980509594874862046961683989710
```
