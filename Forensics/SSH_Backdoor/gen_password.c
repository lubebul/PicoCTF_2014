#include <string.h>
#include <stdio.h>

int main(void) {
  char password[51] = "CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY";
  printf("%s\n", memfrob(strdup(password), strlen(password)));
  
  return 0;
}
