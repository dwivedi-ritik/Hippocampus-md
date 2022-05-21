#include <iostream>
#include <vector>
#include <map>

int main()
{
    std::vector<int> v{9, 6, 4, 2, 3, 5, 7, 0, 1};
    std::map<int, int> range_mapping;
    int size = v.size();
    int key;
    for (auto el : v)
    {
        range_mapping.insert({el, 1});
    }
    for (int i = 0; i <= size; i++)
    {
        if (!(range_mapping.count(i)))
        {
            key = i;
            break;
        }
    }
    std::cout << key << std::endl;
}