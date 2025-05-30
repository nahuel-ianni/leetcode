# Check if a binary string has at most one segment of ones

Given a binary string `s` ​​​​​without leading zeros, return `true​​​` if `s` contains at most one contiguous segment of ones. Otherwise, return `false`.

## Examples
### Example 1
> `Input:` s = "1001"  
> `Output:` false  
> `Explanation:` The ones do not form a contiguous segment.

### Example 2
> `Input:` s = "110"  
> `Output:` true

## Constraints
- `1 <= s.length <= 100`
- `s[i]​`​​​ is either `'0'` or `'1'`.
- `s[0]` is `'1'`.