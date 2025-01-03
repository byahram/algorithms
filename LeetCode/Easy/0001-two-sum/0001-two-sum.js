/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = {};     // map 객체를 생성하고 반복문 수행

     for (let i = 0; i < nums.length; i++) {
        const temp = target - nums[i];      // temp 변수에 target과 nums[i] 뺀 값을 저장

        if(temp in map) {
            return [map[temp], i];
        }

        // map에 key: nums[i], value: i
        map[nums[i]] = i;
    }
};