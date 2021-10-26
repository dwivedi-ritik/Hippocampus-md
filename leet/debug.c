#include <stdio.h>

void main()
{
    char *name = "ritik";
    *(name + 2) = 'p';
    printf("%s\n", name);
}
