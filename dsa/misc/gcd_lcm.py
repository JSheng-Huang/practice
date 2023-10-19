# Refer to:
# GCD: https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html
# LCM: https://mpm580.pixnet.net/blog/post/261336626
# Created by JSheng <jasonhuang0124@gmail.com>
#


# # Euclid's Algorithm.
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    a = 5
    b = 25
    print('a:', a)
    print('b:', b)
    print('GCD of', a, 'and', b, ':', gcd(a, b))
    print('LCM of', a, 'and', b, ':', lcm(a, b))
