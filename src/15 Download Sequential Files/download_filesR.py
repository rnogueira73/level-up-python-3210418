import os
import re
from urllib.parse import urlparse, urlunparse
from urllib.request import urlretrieve

def download_files(url, dirpath):
  os.makedirs(dirpath, exist_ok=True)
  starting_file = urlparse(url)
  first_number = int(re.search(r'\d+', starting_file.path).group())
  common_name = re.search(r'[a-z]+',starting_file.path).group()
  for i in range(100):
    next = f'{common_name+str(first_number + i).zfill(3)}.jpg'
    filename = os.path.join(dirpath,next)
    new_url = urlunparse([starting_file.scheme,starting_file.netloc,next,'','',''])
    try:
      path, headers = urlretrieve(new_url, filename)
      print(f'Downloading {path}')
    except:
      print('\n')
      print(f'{i} files downloaded')
      break


if __name__ == '__main__':
  download_files('http://699340.youcanlearnit.net/image001.jpg','./images')