#include<stdio.h>
#include<stdio.h>
#include <string.h>


void geek(char *S, char *t);
void geek(char *S, char *t)
{
   int i = 0, n = 0;
   char p;
   n = strlen(S);
   while ((p = *S++) != '\0')
   {
      t[n-i] = p;
      i++;
   }
}

int main()
{
   char a[6] = "APPLE";
   char b[6];
   geek(a, b);
   printf("%s", b);
}
