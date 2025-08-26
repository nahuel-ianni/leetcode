# Solution for the 'Add Binary' problem.
# Time complexity: O(m + n).
# Space complexity: O(max(m + n)).

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            total = bit_a + bit_b + carry
            
            # Calculate the new bit and carry
            result.append(str(total % 2))  # Append the result bit (0 or 1)
            carry = total // 2  # Update carry (0 or 1)
            
            i -= 1
            j -= 1
        
        return ''.join(result[::-1])


    # Alternative implementation converting strings to binaries:
    # Potentially less efficient on extremely large numbers.
    # Time complexity: O(m + n).
    # Space complexity: O(1).
    # def addBinary(self, a: str, b: str) -> str:
    #     return format(int(a, 2) + int(b, 2), 'b')
