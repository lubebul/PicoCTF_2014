# Basic ASM
參考資料說AT&T的格式是：<指令> src, dst，所以結果存在第2個operand。把assembly code轉成C code：
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
