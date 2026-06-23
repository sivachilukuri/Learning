def longest_consecutive(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums_set:
        if num -1 not in nums_set:
            current = num
            length = 1
            while current + 1 in nums_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

m = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(m))

def max_subarray_k(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(len(nums)-k):
        curr_sum = curr_sum - nums[i] + nums[i+k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

l = [2, 1, 5, 1, 3, 2]
k = 3
print(max_subarray_k(l, k))

def ispalindrome(s):
    l,r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum(): l += 1
        while l < r and not s[r].isalnum(): r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

k = "A man, a plan, a canal: Panama"
print(ispalindrome(k))

def reverse_integer(x):
    if x < 0:
        sign = -1
        x = x * sign
    else:
        sign = 1
    rev = 0
    n = x
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10
    rev *= sign
    return rev if -2**31 <= rev <= 2**31 - 1 else 0

m = 123
n = -123
print(reverse_integer(m))
print(reverse_integer(n))

def is_Anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in range(len(s)):
        count[s[c]] = count.get(c, 0) + 1
        count[t[c]] = count.get(t[c], 0) - 1
    for v in count.values():
        if v != 0:
            return False
    return True

a = "anagram"
b = "nagaram"
print(is_Anagram(a, b))