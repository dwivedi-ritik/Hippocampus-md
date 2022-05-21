
#include <stdio.h>

int main() {
    int n, x , y , s = 0 , i;
    scanf("%d" , &n);
    scanf("%d" , &x);
    scanf("%d" , &y);
    for(i = 1 ; i <= n ; i++){
        if (i%x == 0 || i%y == 0){
            printf("%d " , i);
            s += i;
        }
    }
    printf("%d" , s);
    
    return 0;
}
