"""1D arrays
"""

import numpy as np

def main():
  """Driven Function
  """
  #create an array
  array = np.array([-2, 1, -5, 10])
  numbers = [-2, 1, -5, 10]
  print(array, type(array))
  print(numbers, type(numbers)) #list output is comma separated
  #convert list into arrays
  new_array = np.array(numbers)
  print(new_array)

  #2D arrays
  matrix = np.array([[-1, 0, 4], [-3, 6, 9]])
  print(matrix)
  print()

  #3D arrays
  array3d = np.array([[[-1, 2, 3],
              [3, 5, 7]],
              [[4, 6, 8],
               [3, 2, 5]]
            ])
  
  print(array3d)

  #using the 'dtype' optional argument to explicitly 
  #declare the data type of the array
  numbers = [-2, 1, -5, 10]
  new_array = np.array(numbers, dtype=np.short)
  print(new_array, new_array.dtype)
  #unsigned data
  pos_numbers = [2, 1, 5, 10]
  new_array = np.array(pos_numbers, dtype=np.ushort)
  print(new_array, new_array.dtype)
  #float data
  numbers = [-2, 1, -5, 10]
  new_array = np.array(numbers, dtype=np.float32)
  print(new_array, new_array.dtype)

if __name__ == '__main__':
  main()