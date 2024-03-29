#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

long long countSubarrays(vector<int>& nums, int k) 
{
        int max_num = *max_element(nums.begin(), nums.end());
        int cnt = 0, n = nums.size();
        long long answer = 0;
        int left = 0;
        for(int right = 0; right < n; right ++)
        {
            cnt +=(nums[right] == max_num);
            while(cnt >= k)
            {
                cnt -= (nums[left++]==max_num);

            }
            answer += 1;
        }

        return answer;
}

int main() {
    std::vector<int> nums = {1,3,2,3,3};
    int k = 2;
    
    long long result = countSubarrays(nums, k);
    
    std::cout << "Number of subarrays where maximum element appears at least " << k << " times: " << result << std::endl;

    return 0;
}