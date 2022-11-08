MONDAY = ('GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE',
          'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN')
TUESDAY = ('ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK',
           'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE')
WEDNESDAY = ('GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE',
             'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE')
THURSDAY = ('BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE',
            'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN')
FRIDAY = ('GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE',
          'RED', 'RED,' 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE')


# QUESTION 1
def mean(MONDAY):
    monday = len(MONDAY)
    total = 0
    for item in monday:
        total += item
    mean = total / len(MONDAY)
    return mean


# QUESTION 2
def mostworn(MONDAY):
    return max(set(MONDAY), key=MONDAY.count)


# QUESTION 3
def median(MONDAY):
    MONDAY.sort()
    if len(MONDAY) % 2 != 0:
        median == MONDAY[int(len(MONDAY)/2)]
    else:
        median = MONDAY[(int(len(MONDAY)/2)) - 1] + MONDAY[int(len(MONDAY)/2)]
        median = median/2
    return median


# QUESTION 8) TO GENERATE RANDOM 4 DIGITS NUMBER OF 0 AND 1, AND CONVERT TO BASE 10
characters = string.digits
random = ''.join(choice(characters) for _ in range(4))

# Converting to base 10


def numtobase(n, b):
    if n == 0:
        return(0)
    digits = ""
    while n:
        digits.append(int(n % b))
        n //= b
        return digits[::-1]


# QUESTION 9) PROGRAM TO SUM FIRST 50 FIBONACCI SEQUENCE
x, y = 0, 1
while y <= 50:
    print(y)
    x, y = y, x+y
