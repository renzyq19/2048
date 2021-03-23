import random

def main():
  grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
  while 2048 not in grid:
    display(grid)
    input()

def display(grid):
  output = ''
  
  for row in grid:
    for num in row:
      output += f'{num} '
    output += '\n'

  print(output)

def randomly_place(grid):
  
if __name__ == '__main__':
  main()
