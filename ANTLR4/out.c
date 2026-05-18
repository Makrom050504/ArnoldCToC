#include <stdio.h>

int main() {
    int isLessThan10 = 1;
    int n = 0;
    while (isLessThan10) {
        n = (n + 1);
        printf("%d\n", n);
        isLessThan10 = (10 > n);
    }
    return 0;
}