"""Test
As title.
Created by JSheng <jasonhuang0124@gmail.com>"""

if __name__ == '__main__':
    """60 = 0011 1100."""
    a = 60

    """13 = 0000 1101."""
    b = 13

    c = 0

    """12 = 0000 1100."""
    c = a & b
    print('60 &(AND) 13:', c)

    """61 = 0011 1101."""
    c = a | b
    print('60 |(OR) 13:', c)

    """49 = 0011 0001."""
    c = a ^ b
    print('60 ^(XOR) 13:', c)

    """-61 = 1100 0011."""
    c = ~a
    print('~60(INVERSE):', c)

    """240 = 1111 0000."""
    c = a << 2
    print('60 << 2:', c)

    """15 = 0000 1111."""
    c = a >> 2
    print('60 >> 2:', c)
