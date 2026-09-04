/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    let duplicate = -1;

    for ( let i = 0; i < nums.length; i++ ) {
        let val = Math.abs( nums[i] );
        if ( nums[val -1] < 0 ) {
            duplicate = val;
        }

        else {
            nums[val -1] *= -1;
        }
    }

    let missing = -1;
    for ( let i =0; i < nums.length; i++ ) {
        if ( nums[i] > 0 ) {
            missing = i + 1;
            break;
        }
    }

    return [duplicate, missing];
};