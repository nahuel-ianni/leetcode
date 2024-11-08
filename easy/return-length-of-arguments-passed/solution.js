/**
 * Solution for the 'Return length of arguments passed' problem.
 * Time complexity: O(1).
 * Space complexity: O(n).
 *
 * @param {...(null|boolean|number|string|Array|Object)} args - Accepts any number of arguments of various types.
 * @return {number} - Returns the number of arguments passed.
 */
var argumentsLength = function(...args) {
    // The length property of the 'args' array represents the number of arguments
    return args.length;
};

// Example usage
// argumentsLength(1, 2, 3); // Output: 3
