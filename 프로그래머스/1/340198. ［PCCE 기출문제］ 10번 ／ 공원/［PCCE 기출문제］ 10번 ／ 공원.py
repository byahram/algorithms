def solution(mats, park):
    R, C = len(park), len(park[0])
    mats.sort(reverse=True)  # 큰 것부터 확인

    for s in mats:
        for i in range(R - s + 1):
            for j in range(C - s + 1):
                ok = True
                for x in range(i, i + s):
                    for y in range(j, j + s):
                        if park[x][y] != "-1":
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    return s
    return -1