#!/usr/bin/python
import math

def mode(n,nums):
    keys = {}
    maxKeyCount = 0
    maxKey = nums[0]
    for x in range(n):
        keys.setdefault(nums[x], 0)
        keys[nums[x]] += 1
        if keys[nums[x]] > maxKeyCount or (keys[nums[x]] == maxKeyCount and nums[x] < maxKey):
            maxKeyCount = keys[nums[x]]
            maxKey = nums[x]
    return maxKey

def median(n,nums):
    nums.sort()
    med = 0
    if n % 2 != 0:
        med = nums[n//2]
    else:
        med = (nums[n//2-1] + nums[n//2]) / 2
    return med

def stdev(n,nums,m):
    sums = 0
    for y in range(n):
        sums += pow(nums[y]-m,2)
    return math.sqrt(sums/n)

def mean(n,nums):
    sums = 0
    for z in range(n):
        sums += nums[z]
    return sums/n

def getStats(n,nums): # ... yeah, it could be prettier
    avg = mean(n,nums)
    print('{0:0.1f}'.format(avg))
    print('{0:0.1f}'.format(median(n,nums)))
    print(mode(n,nums))
    st = stdev(n,nums,avg)
    print('{0:0.1f}'.format(st))
    cinv1 = avg - 1.96*(st/math.sqrt(n)) # 95% z-score
    cinv2 = avg + 1.96*(st/math.sqrt(n))
    print('{0:0.1f} {1:0.1f}'.format(cinv1,cinv2))
    
if __name__ == "__main__":
    n = int(input())
    allNums = input().split(' ')
    nums = [None] * n
    for i in range(n):
        nums[i] = int(allNums[i])
    getStats(n,nums)