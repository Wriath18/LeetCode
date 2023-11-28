nums1 = [-1,0,0,3,3,3,0,0,0]

m = len(nums1)
nums2 = [1,2,2]
n = len(nums2)

def merger(nums1, nums2, m, n):
    nums3 = []
    i = j = 0
    while(i < m and j < n):
        if(nums1[i] <= nums2[j]):
            nums3.append(nums1[i])
            i += 1
        elif(nums1[i] >= nums2[j]):
            nums3.append(nums2[j])
            j+=1
    
    while(i < m):
        nums3.append(nums1[i])
        i += 1
        
    while(j<n):
        nums3.append(nums2[j])
        j += 1
       
    for k in range(len(nums3)):
        nums1[k] = nums3[k]
    

merger(nums1, nums2, 6, 3)

print(nums1)

