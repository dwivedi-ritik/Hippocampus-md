#include <iostream>
#include <string>

class Student
{
public:
    std::string name;

    Student(std::string name)
    {
        this->name = name;
    }
    Student()
    {
        this->name = "Annonymus";
    }

    void greetme()
    {
        std::cout << "Hello " << name << std::endl;
    }
};

int main()
{
    Student s1{"ritik"};
    Student s2;
    s1.greetme();
    s2.greetme();
}