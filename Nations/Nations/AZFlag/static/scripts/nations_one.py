"""
script to parse country names
"""

# function ```nations_py``` 
def nations_py():
  words = []
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  f = open("nations.txt", "r")
  line = f.readline()
  while (line != ""):
    i = 0
    while (line[i] in numbers):
      i += 1
    while (line[i] == " "):
      i += 1
    j = i
    while line[j] != " ":
      j += 1
    words.append(line[i:j])
    line = f.readline()
  f.close()
  f1 = open("data1.txt", "w")
  for j in range(0, len(words)):
    f1.write(words[j])
    f1.write('\n')
  f1.close()
  return

def __main__():
  try:
    nations_py()
  except AttributeError as err:
    print("Attribue error")

__main__()
