def solution(data, ext, val_ext, sort_by):
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    answer = [row for row in data if row[idx[ext]] < val_ext]
    answer.sort(key=lambda x: x[idx[sort_by]])
    return answer