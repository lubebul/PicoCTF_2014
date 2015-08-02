#include <stdio.h>
#include <stdint.h>

#define MAX 8
#define s6MAX 1 << 28

int main(void) {
  uint32_t s_ans[MAX], i;
  
  for (i=0;i<s6MAX;i++) {
    // c9: s5 & 0x70000000 == 0x70000000
    s_ans[5] = (7 << 28) + i;
    // c10, c11
    s_ans[6] = s_ans[5] - 0xe000cec;
    // c8 -> s4
    s_ans[4] = 0x5c483831 - (s_ans[5]*2);
    // c12 -> s7
    s_ans[7] = (0x3726eb17 - (s_ans[4]*3)) / 2;
    // c14 -> s3
    s_ans[3] = 0xb9cf9c91 - (s_ans[7]*3);
    // c4 -> s0
    s_ans[0] = 0x18030607 ^ s_ans[3];
    // c2 -> s1
    s_ans[1] = 0xd5d3dddc - s_ans[0];
    // c1 -> s2
    s_ans[2] = 0xc0dcdfce - s_ans[1];
    // c13 check s2, s7
    if ((s_ans[7]*7) + (s_ans[2]*4) != 0x8b0b922d) continue;
    // c7 check s2, s4
    if ((s_ans[2] * s_ans[4]) != 0x3e436b5f) continue;
    // c5 check s0, s3
    if ((s_ans[0] & s_ans[3]) != 0x666c6970) continue;
    // c3 check s0, s1
    if ((s_ans[1]*5) + (s_ans[0]*3) != 0x404a7666) continue;
    // c6 check s1, s4
    if ((s_ans[4] * s_ans[1]) != 0xb180902b) continue;

    printf("%.*s%.*s%.*s%.*s%.*s%.*s%.*s%.*s\n", 4, (char *)&s_ans[0], 4, (char *)&s_ans[1], 4, (char *)&s_ans[2], 4, (char *)&s_ans[3], 4, (char *)&s_ans[4], 4, (char *)&s_ans[5], 4, (char *)&s_ans[6], 4, (char *)&s_ans[7]);
    break;
  }
  
  return 0;
}
