import pylab

pylab.figure(1) # make figure 1 the current figure
pylab.plot([1,2,3,4], [1,7,3,5]) # draw on figure 1
pylab.title('SimpleVirus Simulation')
pylab.xlabel('Time Steps')
pylab.ylabel('Average Virus Population')   
pylab.show() # show figure on screen
