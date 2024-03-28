#include<iostream>
#include<vector>
using namespace std;

int maxArea(vector<int>& height) 
{
        int n = height.size();
        if (n == 0) return 0;
        int ans = 0;
        int left = 0;
        int right = n-1;

        while(left < right)
        {
            int min_height = min(height[left], height[right]);
            ans = max(ans, min_height * (right-left));
            if(height[left] < height[right])
                left++;
            else
                right--;
        }

        return ans;
}