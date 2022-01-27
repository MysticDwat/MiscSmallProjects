import sys

def centered_average(nums):
    maxn = nums[0]
    minn = nums[0]
    
    total = 0
    count = len(nums)
    
    for num in nums:
        if num > maxn:
            maxn = num
        if num < minn:
            minn = num
        
        total += num
    
    avg = (total - maxn - minn) / (count - 2)
    return int(avg)

t = int(input())

for i in range(1, t + 1):
    k = int(input())
    k_values = []
    
    for j in range(k):
        k_values.append(int(input()))
        
    print(f"Case #{i}:", centered_average(k_values))