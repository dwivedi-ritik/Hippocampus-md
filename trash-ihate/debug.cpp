#include <iostream>
#include <vector>
#include <algorithm>

void ref(int &a, int &b)
{
    std::cout << a << b << std::endl;
}

int main()
{
    std::vector<int> ls{2, 3, 1, 4, 6, 7, 10};
    // std::sort(ls.begin(), ls.end(), std::greater<>());
    // for (auto el : ls)
    // {
    //     std::cout << el << " ";
    // }
    int len = ls.size();

    try
    {
        throw 0;
    }
    catch (const int &e)
    {
        std::cout << e << std::endl;
    }
    int a = 12, b = 34;

    ref(a, b);

    return 0;
}