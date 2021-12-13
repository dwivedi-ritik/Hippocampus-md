#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int arr[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

    //Right row
    int row = 3, col = 4;
    int top = 0, down = row - 1, right = col - 1, left = 0;

    while (top <= down && left <= right)
    {

        for (int i = left, j = top; i <= down; i++)
        {
            cout << arr[i][j] << " ";
        }
        left++;

        for (int i = down, j = left; j <= right; j++)
        {
            cout << arr[i][j] << " ";
        }
        down--;

        for (int i = down, j = right; i >= top; i--)
        {
            cout << arr[i][j] << " ";
        }
        right--;

        for (int i = top, j = right; j >= left; j--)
        {
            cout << arr[i][j] << " ";
        }
        top++;
    }
    cout << endl;

    vector<vector<int>> nums{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    cout << nums.size() << endl;
    cout << nums[0].size() << endl;

    return 0;
}