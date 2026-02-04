def solution(polynomial):
    terms = polynomial.split(" + ")
    answer = []
    x_sum = 0
    const_sum = 0
    
    for term in terms:
        if "x" in term:
            if term == "x":
                x_sum += 1
            else:
                x_sum += int(term[:-1])
        else:
            const_sum += int(term)
    
    if x_sum > 0:
        if x_sum == 1:
            answer.append("x")
        else:
            answer.append(f"{x_sum}x")
    
    if const_sum > 0:
        answer.append(str(const_sum))
    
    return " + ".join(answer)