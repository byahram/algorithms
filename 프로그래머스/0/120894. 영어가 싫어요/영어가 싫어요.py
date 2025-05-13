import re

def solution(numbers):
    # 1.
    # return int(numbers.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0"))
    
    # 2.
    s = ''
    obj = {
        'one': '1',
        'two': '2', 
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    
    for i in re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine)', numbers) :
        s += obj[i]
    return int(s)
    