import re 

def solution(my_string, letter):
    return re.sub(letter, '', my_string)

'''
re.sub('[1-9]', '', "BCBd1112344be")
re.sub('[a-zA-Z]', '', "BCBd1112344be")
re.sub('[a-z]', '', "BCBd1112344be")
'''