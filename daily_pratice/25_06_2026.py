def maxProfit( prices: list[int]) -> int: #121 leetcode problem
        l,r = 0,1 # l=buying price, r=selling price
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

obj = maxProfit([7,1,5,3,6,4])
print(obj)

def productExceptSelf(nums: list[int]) -> list[int]: #238 leetcode problem
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
obj = productExceptSelf([1,2,3,4])
print(obj)

def maxSubArray(nums: list[int]) -> int: #53 leetcode problem
        max_sub = nums[0]
        curr_sub = nums[0]
        for i in nums[1:]:
            if curr_sub < 0:
                curr_sub = 0
            curr_sub = curr_sub + i
            max_sub = max(curr_sub, max_sub)
        return max_sub

obj = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(obj)

def maxProduct(nums: list[int]) -> int: #152 leetcode problem
        res = max(nums)
        curr_min, curr_max = 1,1
        for n in nums:
            if n == 0:
                curr_min,curr_max = 1,1
            temp = curr_max * n
            curr_max = max(n*curr_max, n*curr_min,n)
            curr_min = min(temp, n*curr_min, n)
            res = max(res, curr_max)
        return res
obj = maxProduct([2,3,-2,4])
print(obj)

def findMin(nums: list[int]) -> int: #153 leetcode problem
        res = nums[0]
        l,r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

obj = findMin([3,4,5,1,2])
print(obj)

def search(nums: list[int], target: int) -> int: #33 leetcode problem
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[l]<= nums[mid]:
                if target > nums[mid] or mid < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or mid > nums[l]:
                    r = mid -1
                else:
                    l = mid + 1
        return -1

obj = search([4,5,6,7,0,1,2], 0)
print(obj)