#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int arr[3][3] = {{1, 2, 3}, {5, 6, 7}, {9, 10, 11}};

    int el = 1;
    int row = 3, col = 3;
    int top = 0, down = row - 1, right = col - 1, left = 0;

    while (left <= right && top <= down)
    {
        for (int i = left, j = top; j <= right; j++)
        {
            res[i][j] = el;

            cout << el << " ";
            el++;
        }
        top++;
        for (int i = top, j = right; i <= down; i++)
        {
            // res[i].push_back(el);
            res[i][j] = el;

            cout << el << " ";
            el++;
        }
        right--;

        for (int i = down, j = right; j >= left; j--)
        {
            res[i][j] = el;
            cout << el << " ";
            el++;
        }
        down--;
        for (int i = down, j = left; i >= top; i--)
        {
            // res[i][j] = el;
            cout << el << " ";
            el++;
        }
        left++;
    }
    cout << endl;

    // vector<vector<int>> nums{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    // cout << nums.size() << endl;
    // cout << nums[0].size() << endl;

    return 0;
}