def solution(nums):
    max_num = int(len(nums) / 2)
    mon_types = len(set(nums))
    return min(max_num, mon_types)