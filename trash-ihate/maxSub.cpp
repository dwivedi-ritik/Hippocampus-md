#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int findLength(vector<int>& nums1, vector<int>& nums2) {
        int r = nums1.size();
        int c = nums2.size();

        int table[r+1][c+1] = {0};
        int max_match = 0;

        for( int i =0 ; i < r+1 ; i++){
        	for ( int j = 0 ; j < c+1 ; j++)
        		table[i][j] = 0;
        }

        for(int i = 0 ; i < r+1 ;i++){
            
            for( int j = 0 ; j < c+1 ; j++){
                
                if ( j == 0 )
                    table[i][j] = 0;

                else if( nums1[i-1] == nums2[j-1]) {

                	table[i][j] = 1 + table[i-1][j-1];

                	if (table[i][j] > max_match)
                		max_match = table[i][j];
                }

                
            }
        }

        return max_match;
}


int main()
{
;
	vector<int> n1 = {1,2,3,2,1};
	vector<int> n2 = {3,2,1,4,7};
	cout << findLength(n1 , n2);
}

