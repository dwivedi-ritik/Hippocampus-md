#include <iostream>
#include <vector>
#include <map>
using namespace std;

int longestSequence(vector<int> &nums)
{
    int max = 0;
    int temp, count;
    map<int, bool> nums_maps;
    vector<int> temp_arr;
    for (auto el : nums)
    {
        nums_maps.insert({el, true});
    }
    for (auto el2 : nums)
    {
        if (nums_maps.count(el2 - 1))
        {
            nums_maps[el2] = false;
        }
        else
        {
            temp_arr.push_back(el2);
        }
    }

    for (auto el3 : temp_arr)
    {
        temp = 0, count = 0;
        temp = el3;
        while (nums_maps.count(temp) != 0)
        {
            count++;
            temp++;
        }

        if (count > max)
        {
            max = count;
        }
    }
    return max;
}

int main()
{
    vector<int> nums{100, 4, 200, 1, 3, 2};
    // map<int, bool> m;
    // m.insert({1, true});
    // cout << m.count(2) << endl;
    cout << longestSequence(nums) << endl;
}