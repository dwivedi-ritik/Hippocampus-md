#include <iostream>

using namespace std;

int main()
{
    int t, n, max = -40000;
    cin >> t;
    while (t--)
    {
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            if (arr[i] >= max)
            {
                max = arr[i];
            }
        }
        }
}