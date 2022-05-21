#include <stdio.h>

int bsearch(int arr[], int l, int h, int key)
{
    if (l <= h)
    {
        int m = (l + h) / 2;
        if (arr[m] == key)
            return m;
        else if (arr[m] > key)
            return bsearch(arr, l, m - 1, key);
        else
            return bsearch(arr, m + 1, h, key);
    }
    return -1;
}

void main()
{
    int arr[7] = {1, 2, 3, 4, 5, 6, 7};
    printf("%d\n", bsearch(arr, 0, 6, 7));
}
