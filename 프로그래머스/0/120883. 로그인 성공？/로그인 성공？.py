def solution(id_pw, db):
    users = {}
    for id, pw in db:
        users[id] = pw
    
    input_id, input_pw = id_pw
    
    if input_id not in users:
        return "fail"
    elif users[input_id] != input_pw:
        return "wrong pw"
    else:
        return "login"