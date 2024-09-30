"""Download data from our server
"""

import urllib.request
import zipfile
import os

SERVER_URL = 'https://icarus.cs.weber.edu/~hvalle/cs4580/data/'


def download_file(url, file_name):
  #TODO: Download to pwd

  # TODO: Error checking: Does the url exist?
  urllib.request.urlretrieve(url+file_name, file_name)

  #if we downloaded the file, unzip it
  unzip_file(file_name)
  pass


def unzip_file(file_name):
  cwd = os.getcwd()

  #TODO: make path_to_write, extension variables compatible with files in other directories, e.g. "../data/dataset"
  path_to_write = os.path.join(cwd,file_name).split('.')[0]
  extension = file_name.split('.')[1]


  print(os.path.join(cwd,file_name))

  #check that it is a zip file
  if(extension) == 'zip':
    #check if there is already a directory for that file, if so do not unzip
    print(f'path to write: {path_to_write}')
    if(os.path.exists(path_to_write) == False):
      with zipfile.ZipFile(os.path.join(cwd,file_name), 'r') as zip_ref: #unzips the file
        zip_ref.extractall(file_name.split('.')[0]) #write to a folder that does not have .zip in it
    else:
      print('-----------------------')
      print(f"There are already files at {path_to_write}. \nThe file has not been unzipped to prevent redundancy. \nIf you want to unzip this {file_name}, delete the contents at this directory.")
      print('-----------------------')
  else:
    print(f'File type is .{extension}. This function currently only supports .zip')

  pass


def main():
  """Driven Function
  """

  data = 'pandas01Data.zip'
  download_file(SERVER_URL, data)
  

if __name__ == '__main__':
  main()