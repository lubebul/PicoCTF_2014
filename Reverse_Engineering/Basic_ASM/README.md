# Basic ASM
拿到一個[assembly code](snippet.txt)
 * AT&T的格式：<instr> src, dst
 * 手動把assembly code轉成C code：

```c
#include <stdio.h>

int main() {
  int ebx = 17984;
  int eax = 7205;
  int ecx = 1429;

  if(ebx < eax) {
    ebx *= eax;
    ebx += eax;
    eax -= ecx;
  } else {
    ebx *= eax;
    ebx -= eax;
    eax = ebx;
    eax += ecx;
  }

  printf("%d", eax);

  return 0;
}
```
