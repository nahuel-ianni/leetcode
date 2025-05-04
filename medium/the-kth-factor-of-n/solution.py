# Solution for the 'The kth Factor of n' problem.
# Time complexity: O(√n)
# Space complexity: O(1)

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i

        for i in range((n // 2), 0, -1):
            if n % i == 0 and i != n // i:
                k -= 1
                if k == 0:
                    return n // i

        return -1

    # # Time complexity: O(n)
    # # Space complexity: O(1)
    # def kthFactor(self, n: int, k: int) -> int:
    #     if n < k:
    #         return -1
        
    #     for i in range(1, n + 1):
    #         if n % i == 0:
    #             k -= 1
            
    #         if k == 0:
    #             return i
        
    #     return -1
