/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxTotalValue = function(nums, k) {
    const n = nums.length;
    
    const log2 = new Int32Array(n + 1);
    log2[1] = 0;
    for (let i = 2; i <= n; i++) {
        log2[i] = log2[i >> 1] + 1;
    }
    
    const maxLog = log2[n] + 1;

    const stMax = new Int32Array(n * maxLog);
    const stMin = new Int32Array(n * maxLog);
    
    for (let i = 0; i < n; i++) {
        stMax[i * maxLog + 0] = nums[i];
        stMin[i * maxLog + 0] = nums[i];
    }
    
    for (let j = 1; j < maxLog; j++) {
        for (let i = 0; i + (1 << j) <= n; i++) {
            let leftIdx = i * maxLog + (j - 1);
            let rightIdx = (i + (1 << (j - 1))) * maxLog + (j - 1);
            stMax[i * maxLog + j] = Math.max(stMax[leftIdx], stMax[rightIdx]);
            stMin[i * maxLog + j] = Math.min(stMin[leftIdx], stMin[rightIdx]);
        }
    }

    function queryMax(L, R) {
        const j = log2[R - L + 1];
        return Math.max(stMax[L * maxLog + j], stMax[(R - (1 << j) + 1) * maxLog + j]);
    }

    function queryMin(L, R) {
        const j = log2[R - L + 1];
        return Math.min(stMin[L * maxLog + j], stMin[(R - (1 << j) + 1) * maxLog + j]);
    }
    
    const heapVal = new Int32Array(n);
    const heapL = new Int32Array(n);
    const heapR = new Int32Array(n);
    let heapSize = 0;

    function pushHeap(val, L, R) {
        let i = heapSize++;
        while (i > 0) {
            let p = (i - 1) >> 1;
            if (heapVal[p] >= val) break;
            heapVal[i] = heapVal[p];
            heapL[i] = heapL[p];
            heapR[i] = heapR[p];
            i = p;
        }
        heapVal[i] = val;
        heapL[i] = L;
        heapR[i] = R;
    }

    for (let l = 0; l < n; l++) {
        let val = queryMax(l, n - 1) - queryMin(l, n - 1);
        pushHeap(val, l, n - 1);
    }

    let totalValue = 0; 
    
    for (let i = 0; i < k; i++) {
        let val = heapVal[0];
        let L = heapL[0];
        let R = heapR[0];
        
        totalValue += val;

        if (R > L) {
            let nextR = R - 1;
            let nextVal = queryMax(L, nextR) - queryMin(L, nextR);
            
            let curVal = nextVal, curL = L, curR = nextR, idx = 0;
            
            while ((idx << 1) + 1 < heapSize) {
                let left = (idx << 1) + 1;
                let right = left + 1;
                let largest = left;
                
                if (right < heapSize && heapVal[right] > heapVal[left]) {
                    largest = right;
                }
                if (heapVal[largest] <= curVal) break;
                
                heapVal[idx] = heapVal[largest];
                heapL[idx] = heapL[largest];
                heapR[idx] = heapR[largest];
                idx = largest;
            }
            heapVal[idx] = curVal;
            heapL[idx] = curL;
            heapR[idx] = curR;
        } else {
            let curVal = heapVal[--heapSize];
            let curL = heapL[heapSize];
            let curR = heapR[heapSize];
            
            if (heapSize > 0) {
                let idx = 0;
                while ((idx << 1) + 1 < heapSize) {
                    let left = (idx << 1) + 1;
                    let right = left + 1;
                    let largest = left;
                    
                    if (right < heapSize && heapVal[right] > heapVal[left]) {
                        largest = right;
                    }
                    if (heapVal[largest] <= curVal) break;
                    
                    heapVal[idx] = heapVal[largest];
                    heapL[idx] = heapL[largest];
                    heapR[idx] = heapR[largest];
                    idx = largest;
                }
                heapVal[idx] = curVal;
                heapL[idx] = curL;
                heapR[idx] = curR;
            }
        }
    }
    
    return totalValue;
};