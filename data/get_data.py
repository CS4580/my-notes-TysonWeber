"""Download data from our server
"""

import urllib.request
import zipfile
import os

SERVER_URL = 'https://icarus.cs.weber.edu/~hvalle/cs4580/data/'


def download_file(url, file_name):

  download_folder = "./data"

  # if the data folder does not exist, create one
  if not os.path.exists(download_folder):
    os.makedirs(download_folder)

  # path to download the zip to, in the data folder
  file_path = os.path.join(download_folder, file_name)

  # TODO: Error checking: Does the url exist?
  urllib.request.urlretrieve(url+file_name, file_path)

  # if we downloaded the file, unzip it
  # currently it unzips to the pwd that this get_data.py is called from.

  unzip_file(file_path)


def unzip_file(file_name):
  cwd = os.getcwd()

  #TODO: make path_to_write, extension variables compatible with files in other directories, e.g. "../data/dataset"
  # Currently the file downloads to "./data/"
  path_to_write = "./data"
  # extension = file_name.split('.')[-1]


  print(f'extracting {file_name} to ' + os.path.join(cwd,file_name))

  # below logic doesn't quite qork
  # #check that it is a zip file
  # if(extension) == 'zip':
  #   #check if there is already a directory for that file, if so do not unzip
  #   print(f'path to write: {path_to_write}')
  with zipfile.ZipFile(os.path.join(cwd,file_name), 'r') as zip_ref: #unzips the file
    zip_ref.extractall(path_to_write) #write to a folder that does not have .zip in it
    
  # else:
  #   print(f'File type is .{extension}. This function currently only supports .zip')

  pass


def main():
  """Driven Function
  """

  data = 'pandas01Data.zip'
  download_file(SERVER_URL, data)
  

if __name__ == '__main__':
  main()