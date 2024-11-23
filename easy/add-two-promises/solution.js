/*
 * Solution for the 'Add Two Promises' problem.
 * Time complexity: O(1) assuming the promises resolve instantly; 
 * otherwise depends on the duration of the promises.
 * Space complexity: O(1).
 *
 * @param {Promise<number>} promise1 - A promise that resolves to a number.
 * @param {Promise<number>} promise2 - A promise that resolves to a number.
 * 
 * @return {Promise<number>} - A promise that resolves to the sum of the two numbers.
 */

var addTwoPromises = async function(promise1, promise2) {
    // Use Promise.all to execute both promises in parallel and wait for both to resolve.
    // Then destructure the resolved values and return their sum.
    return Promise.all([promise1, promise2])
                  .then(([value1, value2]) => value1 + value2);
};

// Example usage
// addTwoPromises(Promise.resolve(2), Promise.resolve(2)).then(console.log); // Output: 4
