#include<iostream>
#include<vector>
using namespace std;

int minSubArrayLen(int target, vector<int>& nums) 
{
        int n = nums.size();
        int window = 0;
        int ans = n+1;
        int left = 0;

        for(int right=0;right<n;right++)
        {
            window += nums[right];
            while(window >= target)
            {
                ans = min(ans, right - left + 1);
                window -= nums[left++];
            }
        }

        if(ans == n+1)
        {
            return 0;
        }
        else
        {
            return ans;
        }
}