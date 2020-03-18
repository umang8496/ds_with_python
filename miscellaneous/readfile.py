import os.path

filename='D:/Python/PyPrograms/readwrite.txt'

if not os.path.isfile(filename):
     print("file does not exist")

else:
     with open(filename) as f:
          content=f.readlines()
          #content=f.read().splitlines()

     for line in content:
          print(line)
