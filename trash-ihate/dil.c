#include <stdio.h>
int main()
{
    int arr[6] = {5, 5, 1, 2, 3, -4};
    int s = 0, flag = 0;

    for (int i = 0; i < 6; i++)
    {
        s = arr[i];
        for (int j = i + 1; j < 6; j++)
        {
            s += arr[j];
            if (s == 0)
            {
                printf("1\n");
                flag++;
                break;
            }
        }
        if (flag == 1)
        {
            break;
        }
    }
    if (flag == 0)
    {
        printf("0");
    }
    return 0;
}
