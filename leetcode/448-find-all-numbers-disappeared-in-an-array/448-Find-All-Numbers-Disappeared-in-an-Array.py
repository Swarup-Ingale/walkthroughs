/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    for ( let i = 0; i < nums.length; i++ ) {
        let targetIdx = Math.abs( nums[i] ) - 1;
        if ( nums[targetIdx] > 0 ) {
            nums[targetIdx] *= -1;
        }
    }

    const ans = [];
    for ( let i = 0; i < nums.length; i++ ) {
        if ( nums[i] > 0 ) {
            ans.push( i + 1 );
        }
    }

    return ans;
};