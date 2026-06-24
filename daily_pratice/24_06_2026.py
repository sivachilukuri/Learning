def ispalindrome(s):
    l,r = 0,len(s)-1
    while l < r:
        if s[l] != s[r]:
            skipr =s[l+1:r+1]
            skipl =s[l:r]
            return skipr == skipr[::-1] or skipl == skipl[::-1]
        l += 1
        r -= 1
    return True

obj = ispalindrome("eyae")
print(obj)

def sqrt(x):
    l,r = 0, x
    res = 0
    while l <= r:
        m = l + ((r-1)//2)
        if m **2 > x:
            r = m - 1
        elif m**2 < x:
            l = m + 1
            res = m
        else:
            return m
    return res

obj = sqrt(8)
print(obj)

def findmissingandrepetative(grid: List[List[int]]) -> List[int]:
    n = len(grid)
    count = {}
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in count:
                count[grid[i][j]] = 0
            count[grid[i][j]] += 1
    double, missing = 0,0
    for num in range(1, n*n+1):
        if num not in count:
            missing = num
        elif count[num] == 2:
            double = num
    return [double,missing]

obj = findmissingandrepetative([[1,2],[2,4]])
print(obj)

def removestarts(s:str):
    stack = []
    for c in s:
        if c == "*":
            stack and stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

obj = removestarts("abc*de**f")
print(obj)

def removeduplicates(nums: List[int]) -> int:
    l,r = 0,0
    while r < len(nums):
        count = 1
        while r+1 < len(nums) and nums[r]==nums[r+1]:
            r += 1
            count += 1
        for i in range(min(2,count)):
            nums[l]=nums[r]
            l += 1
        r += 1
    return l

obj = removeduplicates([1,1,1,2,2,3])
print(obj)