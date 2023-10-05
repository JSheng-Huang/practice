# Refer to: https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html
#
# Created by JSheng <jasonhuang0124@gmail.com>
#


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


def lcm():
    pass


if __name__ == '__main__':
    a = 50
    b = 100
    print('a:', a)
    print('b:', b)
    print('GCD of', a, 'and', b, ':', gcd(a, b))
