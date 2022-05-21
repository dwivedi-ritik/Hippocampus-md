#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

std::string findDifferentBinaryString(std::vector<std::string> &nums)
{
    std::map<int, std::string> table;
    int temp;
    for (auto s : nums)
    {
        temp = std::stoi(s, 0, 2);
        table.insert({temp, s});
    }
    int n = (nums.at(0)).length();
    int start_range = std::pow(2, n - 1);
    int last_range = std::pow(2, n) - 1;
    int key = 0;

    for (int i = start_range; i <= last_range; i++)
    {
        if (!(table.count(i)))
        {
            key = i;
            break;
        }
    }

    int mask = 1;
    std::string binary;
    for (int i = 0; i < n; i++)
    {
        if ((mask & key) >= 1)
            binary = "1" + binary;
        else
            binary = "0" + binary;
        mask <<= 1;
    }
    return binary;
}
int main()
{
    std::vector<std::string> v1{"0"};

    std::cout << findDifferentBinaryString(v1) << std::endl;
    return 0;
}