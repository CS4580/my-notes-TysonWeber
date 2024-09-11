"""Array operations
"""
import numpy as np

def main():
  """Driven Function
  """
  numbers_list = [2,4,6,8,10]
  #cumbersome using a range based loop
  print(f'Before list: {numbers_list}')
  for x in range(len(numbers_list)):
    numbers_list[x] = numbers_list[x]+3
  
  print(f'After list: {numbers_list}')

  #using a numpy array
  numbers_arr = np.array(numbers_list)
  print(f'Before array: {numbers_arr}')
  numbers_arr = numbers_arr + 3
  print(f'After array: {numbers_arr}')

if __name__ == '__main__':
  main()