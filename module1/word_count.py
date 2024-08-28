"""Read file from web and do analysis of data
"""

import urllib.request

# link = "http://www.somesite.com/details.pl?urn=2344"
# f = urllib.request.urlopen(link)
# myfile = f.read()


def main():
  """Driven Function
  """
  
  file_address = 'https://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
  words = countWords(file_address)
  print(f'There are a total of {words} words in the file')


def countWords(url_address):
  words = 0
  # file = urllib.request.urlopen(filename)
  # file_text = file.read()

  #open the file, and read each line
  with urllib.request.urlopen(url_address) as data:
    for line in data:
      # print(line, type(line))
      line = line.decode('utf-8')
      # print(line, type(line))
      #for every line in the file, split into individual words, then increment count for each word in the split
      line_words = line.split()
      words += len(line_words)
      # for word in line_words:
      #   words += 1

  return words
   

if __name__ == '__main__':
  main()