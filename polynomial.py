import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def ferror(param,data):
  x=data[0]
  y=data[1]
  y0=np.polyval(param,x)
  err = np.sum((y-y0)**2)
  return err

def test_run():
  orig=[1.5,-10.,-5.,60.,50.]
  x=np.linspace(-5,5,21)
  y_org=np.polyval(orig,x)
  data = [x,y_org]
  guess=np.ones(5)
  sol=spo.minimize(ferror,guess,args=(data,),method='SLSQP')
  solution=sol.x
  print 'original parameters:',orig
  print '   guess parameters:',guess
  print 'solution parameters:',solution
  y_guess=np.polyval(guess,x)
  y_sol = np.polyval(solution,x)
  plt.plot(x,y_org,'go',label='ORIGINAL')
  plt.plot(x,y_guess,'b--',label='GUESS')
  plt.plot(x,y_sol,'r--',label='SOLUTION')
  plt.legend(loc='upper right')
  plt.show()

test_run()
