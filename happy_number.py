"""
19 = 1*1 + 9*9 = 82

"""

def happyNumber(n):
    def findPow(n):
        ans = 0
        while n:
            rem = n%10
            ans = ans+(rem*rem)
            n = n//10
        return ans
    slow = n
    fast = n
    slow = findPow(n)
    fast = findPow(findPow(n))
    if slow==1:
        return True
    while slow!=fast:
        slow = findPow(slow)
        fast = findPow(findPow(fast))
        if slow==fast:
            return False
        if slow==1 or fast==1:
            return True

print(happyNumber(19))


