"""Library to calculate number of digits
for different algorithms
"""
import math

def factorial_length(number):
  """Count the number of digits in a factorial number

  Args:
      number (int): integer value to calculate factorial

  Returns:
      int: number of digits for factorial of input
  """

  """take the factorial of the number, then take log 10 of that number. 
  Log 10 counts the number of 10s we have (10^x)
    then we have to take the ceiling of this number to get the integer number of digits"""
  #length = math.ceil(math.log10(math.factorial(number)))
  #return length

  #alternatively...
  length = math.factorial(number) 
  length = str(length) # convert to str
  return len(length) #return the number of elements


def main():
  """Driven Function
  """
  print('Main Function')
  number = 120
  digits = factorial_length(number)
  print(f'You have {digits} digits in factorial({number})')



if __name__ == '__main__':
  main()