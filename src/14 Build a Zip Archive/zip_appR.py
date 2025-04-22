from zipfile import ZipFile
import os

def zip_all(path, extentions, zipfile):
  filePaths = []
  for root, _, files in os.walk(path):
    for filename in files:
      _, ext = os.path.splitext(filename)
      if ext in extentions:
        filepath = os.path.join(root, filename)
        filePaths.append(filepath)


  with ZipFile(zipfile, 'w') as myzip:
    for file_name in filePaths:
      myzip.write(file_name)

if __name__ == '__main__':
  zip_all('src/14 Build a Zip Archive/my_stuff',['.jpg','.txt'],'my_stuff.zip')