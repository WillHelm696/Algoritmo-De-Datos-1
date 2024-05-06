from algo1 import *

def search(Array, element):
  i = 0
  flag = False
  while flag != True:
    if i == len(Array):
      flag = True
    elif element == Array[i]:
      return i
    i += 1
  return None

def delete(Array, element):
  x = search(Array, element)
  if x != None:
    for i in range(x, len(Array)-1):
      Array[i] = Array[i+1]
    Array[len(Array)-1] = None
    return x
  else:
    return None    

def insert(Array, element, position):
  if position >= 0 and position < len(Array):
    i = len(Array)-1
    while i != position:
      Array[i] = Array[i-1]
      i -= 1
    Array[position] = element
    return position
  else:
    return None

def length(Array):
  count = 0
  for i in range(0, len(Array)):
    if Array[i] != None:
      count += 1
  return count
