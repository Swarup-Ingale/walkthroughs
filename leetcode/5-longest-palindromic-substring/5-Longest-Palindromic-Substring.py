/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if ( !s || s.length === 0 ) return "";

    let start = 0;
    let end = 0;

    const expandAroundCenter = ( left, right ) => {
        while ( left >= 0 && right < s.length && s[left] === s[right] ) {
            left--;
            right++;
        }

        return right - left - 1;
    };

    for ( let i = 0; i < s.length; i++ ) {
        const len1 = expandAroundCenter( i, i );
        const len2 = expandAroundCenter( i, i + 1 );

        const maxLength = Math.max( len1, len2 );
        if ( maxLength > end - start + 1 ) {
            start = i - Math.floor( ( maxLength - 1 ) / 2 );
            end = i + Math.floor( maxLength / 2 );
        }
    }

    return s.slice( start, end + 1 );
};