#!/usr/bin/python
movefile = open('directions','r')
directions = movefile.read().rstrip().split(", ")
x = 0
y = 0
facing = 0
# 0 = North
# 1 = East
# 2 = South
# 3 = West
for direction in directions:
  #print(direction)
  turning = direction[0]
  blocks = int(direction[1:])
  #print(direction +": turn " + turning + ", go " + blocks + " blocks")
  if turning == "L":
    facing = facing - 1
  else:
    facing = facing + 1
  if facing < 0:
    facing = 3
  if facing > 3:
    facing = 0

  if facing == 0:
    y = y + blocks
    print(direction + ": went North " + str(blocks) + " blocks.")
  if facing == 1:
    x = x + blocks
    print(direction + ": went East " + str(blocks) + " blocks.")
  if facing == 2:
    y = y - blocks
    print(direction + ": went South " + str(blocks) + " blocks.")
  if facing == 3:
    x = x - blocks
    print(direction + ": went West " + str(blocks) + " blocks.")
print (str(y) + " vertical and " + str(x) + " horizontal is " + str(abs(x) + abs(y)) + " blocks.")
