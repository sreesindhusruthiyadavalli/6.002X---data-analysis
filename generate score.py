import random, pylab


    
def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    scores = []
    for i in range(numTrials):
        m1 = random.uniform(50, 81)
        m2 = random.uniform(60, 91)
        f = random.uniform(55, 96)
        score = 0.25 * (m1 + m2) + 0.5 * f
        scores.append(score)
    mean = 0.0
    for score in scores:
        mean = mean + score
    scores.append(mean / float(numTrials))
    return scores 
    
def plotQuizzes():
    # Your code here
    #pass
    numTrails = 10000
    FinalScore = generateScores(numTrails)
    pylab.figure()
    pylab.plot(FinalScore)
    pylab.plot(numTrails)
    pylab.hist(FinalScore, bins = 7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials') 
    pylab.show()         

plotQuizzes()
