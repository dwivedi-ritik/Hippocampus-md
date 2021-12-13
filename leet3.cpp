#include <iostream>
#include <map>
#include <vector>
//Finding duplicate in an array

int main()
{
    std::vector<int> v{3, 1, 3, 4, 2};
    std::map<int, int> entry;

    int key;
    for (auto n : v)
    {
        if (entry.count(n))
        {
            key = n;
            break;
        }
        else
        {
            entry.insert({n, 1});
        }
    }
}