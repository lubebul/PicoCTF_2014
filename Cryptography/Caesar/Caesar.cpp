#include <stdio.h>
#include <string.h>

#define MAX 100

int main () {

    char str[MAX] = "uiftfdsfuqbttqisbtfjtpgtqyrdhekuqsxjdtvyvkghlpvkfml";

    for(int i=0;i<26;i++) {
        for(int j=0;j<strlen(str);j++)
            printf("%c", (str[j]-'a'+i)%26+'a');
        printf("\n");
    }

    return 0;
}
