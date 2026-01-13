import math

def solution(numer1, denom1, numer2, denom2):
    bunja = (denom1 * numer2) + (numer1 * denom2)
    bunmo = denom1 * denom2
    
    g = math.gcd(bunja, bunmo)
    bunja //= g
    bunmo //= g

    return [bunja, bunmo]