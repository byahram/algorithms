/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const map = new Map();  // map 키-값 쌍을 저장하는 자료구조 

    for(let i = 0; i < nums.length; i++) {
        if(i - map.get(nums[i]) <= k) {     // map.get(nums[i]): 해당 숫자가 저장된 이전 인덱스
            return true;
        }
        map.set(nums[i], i);    // 키는 nums의 숫자값, 값은 해당숫자가 마지막으로 등한 인덱스
    }
    return false;
};

/**
 * 시간 복잡도 O(n), 공간 복잡도 O(n)
 */