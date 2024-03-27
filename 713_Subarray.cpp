#include<iostream>
#include<vector>
using namespace std;

int numSubarrayProductLessThanK(vector<int>& nums, int k) 
{
        int n = nums.size();
        if (n == 0 || k <= 1 || k == 0) return 0;
        int window = 1;
        int ans = 0;
        int left = 0;

        for(int right=0;right<n;right++)
        {
            window *= nums[right];
            while(window >= k)
            {
                
                window /= nums[left++];
            }
            ans += (right - left + 1);
        }

        return ans;
}