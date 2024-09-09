"""Practice creating arrays from ranges
"""

import numpy as np

def main():
  """Driven Function
  """
  #generate 1D arrays from 0 to 8
  array = np.arange(9)
  print(array)
  #you may have negative numbers
  array = np.arange(-4,4)
  print(array)
  #add a step to each increment
  array = np.arange(-8, 8, 2)
  print(array)

  #generate acn array with values from 0 to 5, in steps of 0.1
  array = np.arange(0, 5, .1)
  print(array)
  #ranges with decimal values
  array = np.arange(0.1, 0.3, 0.01)
  print(array)

  #reivew lecture and fill in rest of notes

 

if __name__ == '__main__':
  main()