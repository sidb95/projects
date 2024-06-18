"""
sort country names
"""

# function ```nations_py``` 
def nations_sort():
  f = open('../files/nations.txt', 'r')
  line = f.readline()
  nations = []
  while line != "":
    nations.append(line)
    line = f.readline()
  f.close()
  nations.sort()
  f = open('../files/nations_sorted.txt', 'w')
  for nation in nations:
    f.write(nation)
  f.close()

def __main__():
  nations_sort()

__main__()
