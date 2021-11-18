#include <stdio.h>

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int arr[10] = {3, 11, 12, 8, 5, 7, 12, 16, 1, 9};
    //Shell Sort my implementation
    int n = 10;

    for (int gap = n / 2; gap != 0; gap = gap / 2)
    {
        for (int i = 0, j = gap; j < n; j++, i++)
        {
                }
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}