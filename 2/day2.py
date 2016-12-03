#!/usr/bin/python
patterns = [movesfile.rstrip('\n') for movesfile in  open('pattern', 'r')]
point = 5
for pattern in patterns:
  #print pattern
  for move in pattern:
    if move == "U" and not point in (1,2,3):
        point = point - 3
    if move == "D" and not point in (7,8,9):
        point = point + 3
    if move == "R" and not point in (3,6,9):
        point = point + 1
    if move == "L" and not point in (1,4,7):
        point = point - 1
  print("Number - " + str(point))
       
  

