import random
def sampleQuizzes():
    # Your code here
    n = 10000
    yes = 0
    for i in range(n):
        m1 = random.uniform(50, 81)
        m2 = random.uniform(60, 91)
        final = random.uniform(55, 96)
        score = 0.25 * (m1 + m2) + 0.5 * final
        if 70 <= score <=75:
            yes = yes + 1
    return yes / float(n)        
        
