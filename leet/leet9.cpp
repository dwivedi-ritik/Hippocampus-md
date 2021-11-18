#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isAnna(string s1, string s2)
{
    vector<int> chars(25, 0);

    int len = s1.size();

    if (s1.size() != s2.size())
        return false;

    for (int i = 0; i < len; i++)
    {
        int s1_index = 97 - s1[i];
        int s2_index = 97 - s2[i];

        cout << s1_index << endl;
        // chars[s1_index] += 1;
        // chars[s2_index] -= 1;
    }

    for (int j = 0; j < 26; j++)
    {
        if (chars[j] != 0)
            return false;
    }
    return true;
}

int main()
{
    string a = "abc";
    string b = "bab";
    cout << isAnna(a, b) << endl;
    // vector<string> v{"eat", "tea", "tan", "ate", "nat", "bat"};
    // vector<vector<string>> res;
    // vector<string> temp;
    // int i = 0, j = 0;
    // int len = v.size();

    // while (i < len)
    // {
    //     j = i + 1;
    //     if (v[i] != "$")
    //     {
    //         temp.push_back(v[i]);
    //         while (j < len)
    //         {
    //             if (v[j] != "$")
    //             {
    //                 if (isAnna(v[i], v[j]))
    //                 {
    //                     temp.push_back(v[j]);
    //                     v[j] = "$";
    //                 }
    //             }
    //             j++;
    //         }
    //         res.push_back(temp);
    //         temp.clear();
    //     }
    //     i++;
    // }
    // for (auto el : res)
    // {
    //     for (auto p : el)
    //     {
    //         cout << p << endl;
    //     }
    // }
    // return 0;
}