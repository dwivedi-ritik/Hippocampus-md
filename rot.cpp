#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

//Rotating any array to right

int main()
{
    vector<int> arr{1, 2, 3, 4, 5, 6, 7};
    int k = 3;

    for (auto el : arr)
    {
        cout << el << " ";
    }
    cout << endl;

    int n = arr.size();

    for (int i = 0, j = n - k - 1; i < j; i++, j--)
    {
        swap(&arr[i], &arr[j]);
    }

    for (int i = n - k, j = n - 1; i < j; i++, j--)
    {
        swap(&arr[i], &arr[j]);
    }

    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        swap(&arr[i], &arr[j]);
    }
    for (auto el : arr)
    {
        cout << el << " ";
    }
    cout << endl;
}