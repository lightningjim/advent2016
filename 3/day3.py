#!/usr/bin/python
triangles = [trifile.rstrip('\n') for trifile in open('triangles')]
valid = 0
for triangle in triangles:
  sides = triangle.strip().split(' ');
  sides = [x for x in sides if x != '']
  sides = map(int,sides)
  sides.sort()
  if sides[0] + sides[1] > sides[2]:
    valid = valid + 1
print valid
  
  
