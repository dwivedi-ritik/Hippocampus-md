#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isAnna(string s1, string s2)
{
    vector<int> chars(25, 0);

    int len = s1.length();

    if (s1.length() != s2.length())
        return false;

    for (int i = 0; i < len; i++)
    {
        chars[97 - s1[i]] = chars[97 - s1[i]] + 1;
        chars[97 - s2[i]] = chars[97 - s1[i]] - 1;
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
    vector<string> v{"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> res;
    vector<string> temp;
    int i = 0, j = 0;
    int len = v.size();

    while (i < len)
    {
        j = i + 1;
        if (v[i] != "$")
        {
            temp.push_back(v[i]);
            while (j < len)
            {
                if (v[j] != "$")
                {
                    if (isAnna(v[i], v[j]))
                    {
                        temp.push_back(v[j]);
                        v[j] = "$";
                    }
                }
                j++;
            }
            res.push_back(temp);
            temp.clear();
        }
        i++;
    }
    for (auto el : res)
    {
        for (auto p : el)
        {
            cout << p << endl;
        }
    }
    return 0;
}