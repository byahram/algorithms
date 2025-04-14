def solution(array, height):
    # 1
    # count = 0
    # for i in array :
    #     if i > height :
    #         count += 1
    # return count      
    
    # 2
    array.append(height)
    return sorted(array, reverse=True).index(height)
   