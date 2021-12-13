#include <iostream>
#include <string>

int main()
{
    std::string s1{"to end of the worldlife"};
    //Removing leading and trailing spaces
    int start = s1.find_first_not_of(" ");
    int end = s1.find_last_not_of(" ");

    // std::cout << start;
    std::string new_string;
    new_string = s1.substr(start, end - start + 1);

    int len = new_string.length();

    int max = 0;

    for (int i = 0; i < len; i++)
    {
        if (new_string.at(i) == ' ')
        {
            max = i + 1;
        }
    }
    std::cout << len - max << std::endl;
}