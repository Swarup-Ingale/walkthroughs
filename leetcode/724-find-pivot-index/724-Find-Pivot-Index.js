/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let total = 0;
    for (const x of nums) {
        total += x;
    }

    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        const rightSum = total - leftSum - nums[i];
        if (leftSum === rightSum) {
            return i;
        }
        leftSum += nums[i];
    }

    return -1;
};