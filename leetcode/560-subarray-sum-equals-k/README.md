# 560. Subarray Sum Equals K

🟡 **Medium** &nbsp;|&nbsp; [View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)

**Topics:** Array, Hash Table, Prefix Sum

---

<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the total number of subarrays whose sum equals to</em> <code>k</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3], k = 3
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>


---

**My Solution:** [560-Subarray-Sum-Equals-K.py](./560-Subarray-Sum-Equals-K.py)



## Just a sneak peak and reminder for tomorrow:

How It Works (The Logic)A prefix sum (t in your code) is the cumulative sum of all elements from the start of the array up to the current index. If the sum of a subarray between two indices equals \[k\], then mathematically:\[\text{Current\ Prefix\ Sum}-\text{Previous\ Prefix\ Sum}=k\]Rearranging this formula gives: \[\text{Previous\ Prefix\ Sum}=\text{Current\ Prefix\ Sum}-k\]sub_num = {0:1}: This handles the edge case where a prefix sum itself perfectly equals \[k\]. It means "we have seen a prefix sum of 0 exactly 1 time before starting." if t - k in sub_num: At any point, if t - k exists in our dictionary, it means a valid previous subarray exists that can be subtracted from our current tracking to form exactly \[k\]. We add the frequency of that previous sum to our counter c. sub_num[t] = 1 + sub_num.get(t, 0): We update our dictionary with the current prefix sum so it can be used by future elements. The Pattern to Remember: "Prefix Sum + Hash Map"This is a classic LeetCode pattern. You should immediately think of it whenever a problem asks you to find contiguous subarrays matching a specific criteria (like a target sum, a multiple of a number, or equal counts of elements). Core Blueprint Track Cumulative Progress: Maintain a running variable as you loop through the array (e.g., cumulative sum, running balance of 0s and 1s, or cumulative remainder). Look Backward Using a Map: Use a hash map to store  { Seen_State : Frequency_or_Index }. Check the Match Condition: At each step, calculate the "required past state" needed to satisfy your target criteria (\(CurrentState - Target\)). Check if that past state exists in your map. Common Problems Using This Exact Pattern LeetCode 560: Subarray Sum Equals K (This one)LeetCode 525: Contiguous Array (Find max length of binary subarray with equal 0s and 1s) → Pattern: Treat 0 as -1, find subarray sum equal to 0.LeetCode 974: Subarray Sums Divisible by K → Pattern: Track cumulative prefix sum remainders (prefix_sum % k).LeetCode 325: Maximum Size Subarray Sum Equals k 
