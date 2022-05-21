#include <stdio.h>

void main()
{
    //Implementation of quick sort
    int n, max = -1, pos;
    scanf("%d", &n);

    int arr[n];
    printf("Enter the values of array: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }

    //Initializing each array element with 0 in counter array
    int counterArray[max + 1];
    for (int i = 0; i < max; i++)
        counterArray[i] = 0;

    for (int i = 0; i < n; i++)
    {
        pos = arr[i];
        counterArray[pos] += 1;
    }

    //Prinitng sorted array
    for (int i = 0; i < max; i++)
    {
        while (counterArray[i] != 0)
        {
            printf("%d ", i);
            counterArray[i] -= 1;
        }
    }
}