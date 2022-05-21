#include <stdio.h>

int atoi(char *num)
{
    int res = 0;
    for (int i = 0; num[i] != '\0'; i++)
    {
        res = res * 10 + (num[i] - 48);
    }
    return res;
}

char *multiply(char *num1, char *num2)
{
    long temp_num1 = atoi(num1);
    long temp_num2 = atoi(num2);
    long long res = temp_num1 * temp_num2 ;

    int count 
}
int main()
{
    int num = 131123;
    while (num != 0)
    {
        printf("%d\n", num % 10);
        num = num / 10;
    }
    printf("%d\n", '2' - 48);

    printf("%d\n", atoi("2131"));
}