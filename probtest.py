def probTest(limit):
    #pass
    x = 1
    prob = 1.0 / 6
    while prob > limit:
        prob = float((5 ** x)) / (6 ** (x + 1))
        x = x + 1
    return x
