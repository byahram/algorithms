def solution(phone_book):
    hash_map = {number:True for number in phone_book}
    
    for phone_number in phone_book:
        prefix = ""
        for char in phone_number:
            prefix += char
            
            if prefix in hash_map and prefix != phone_number:
                return False
    return True