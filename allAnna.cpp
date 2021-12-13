#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int is_anna(string s1, string s2)
{
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    if (s1 == s2)
        return 1;

    return 0;
}

int main()
{
    string a = "abc";
    string b = "aba";

    cout << is_anna(a, b) << endl;
    return 0;
}