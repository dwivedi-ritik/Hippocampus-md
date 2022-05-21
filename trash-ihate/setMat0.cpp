#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int notin(vector<int> arr, int key)
{
    for (int el : arr)
    {
        if (el == key)
            return false;
    }
    return true;
}

void setMat(vector<vector<int>> &mat)
{
    int r = mat.size();
    int c = mat[0].size();
    int i, j;
    vector<int> row;
    vector<int> col;
    for (i = 0; i < r; i++)
    {
        row.push_back(-1);
    }

    for (i = 0; i < c; i++)
    {
        col.push_back(-1);
    }

    // Show matrix

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    //  Implementation

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            if (mat[i][j] == 0)
            {
                row[i] = 0;
                col[j] = 0;
            }
        }
    }

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            if (row[i] == 0 || col[j] == 0)
            {
                mat[i][j] = 0;
            }
        }
    }
    //  Final
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    vector<vector<int>> matrix = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};

    // vector<vector<int>> matrix = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
    // vector<vector<int>> matrix = {{1, 2, 3, 4},
    //                               {5, 0, 7, 8},
    //                               {0, 10, 11, 12},
    //                               {13, 14, 15, 0}};
    setMat(matrix);
    return 0;
}