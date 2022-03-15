from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import cmath as bmath
import itertools

class plot():
  def __init__(self,fig,ax):
      self.fig = fig
      self.ax = ax
      self.scatter = make_plot([-10,10],[-10,10])
  
  def resize(self,event):
    print('clicked')
    self.scatter.remove()
    self.scatter = make_plot(self.ax.get_xbound(),self.ax.get_ybound())


def f(x,roots):
  ex = 1
  for i in roots:
    ex = ex*(x+i) 


def f_prime(x,roots):
  things = list(map(lambda x,root:(x-root),[x]*len(roots),[x]*len(roots),roots))
  return(sum(itertools.permutations(things,len(things)-1)))


def newtons_method(x,roots):
  while True:
    f_p=f_prime(x,roots) 
    fn = f(x,roots)
    if abs(fn)<= .00001:
      return(x)
    if f_p == 0:
      return(0)
    if abs(fn) > 10000:
      return(0)
    x=x-fn/f_p

def find_roots():
  done = False
  roots = []
  while not done:
    roots.append(input('enter a root '))
    if input('done? ') == 'yes':
      done = True
  return(roots)


def colorize(y,roots):
  return(['white','red','green','blue'][min_index(list(map(lambda root:abs(root-y),roots)))])


def min_index(jimbo):
  return(jimbo.index(min(jimbo)))


def make_plot(x,y):
  roots = [find_roots()]
  x = np.arange(x[0],x[1],(x[1]-x[0])/50)
  y = np.arange(y[0],y[1],(y[1]-y[0])/400)
  x1,x2 = np.meshgrid(x,y)
  cx = list(map(complex,x1.flatten(),x2.flatten()))
  roots = [roots]*len(cx)
  root = list(map(newtons_method,cx)) 
  c = list(map(colorize,root,roots))
  return(plt.scatter(x1.flatten(),x2.flatten(),c = c,s = 1,marker = '.'))


def main():
  fig,ax = plt.subplots()
  p = plot(fig,ax)
  p.fig.canvas.mpl_connect('button_release_event',p.resize)
  plt.show()

make_plot([-10,10],[-10,10])