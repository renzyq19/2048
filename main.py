import random

VALID_DIRECTIONS = ['UP','DOWN','LEFT','RIGHT']
size = 4


class Cell():
  def __init__(self, up=None, down =None, left=None, right=None):
    self.up = up
    self.right = right
    self.left = left
    self.down = down
    self.value = 0
    self.merged = False

  def __str__(self):
    return str(self.value) if self.value else ' ' 
    
  def __repr__(self):
    return f"Cell(value = {self.value},{self.up},{self.right},{self.down},{self.left})"
    
  def should_move(self):
    return bool(self.value)
    
  def can_move_into(self, direction):
    target = getattr(self,direction.lower())
    if not target:
      return None
    elif not target.value:
      return self.move_into
    elif target.value != self.value:
      return None
    elif target.value == self.value and (self.merged or target.merged):
      return None
    elif target.value == self.value: 
      return self.merge_into


  def merge_into(self,direction):
    other = getattr(self,direction.lower())
    other.value *= 2
    self.value = 0
    other.merged = True
  
  def move_into(self,direction):
    other = getattr(self,direction.lower())
    other.value = self.value
    self.value = 0
    other.merged = self.merged
    

    
  



def main():
  grid = generate_grid()
  while 2048 not in grid:
    reset_merged_status(grid)
    randomly_place(grid)
    randomly_place(grid)
    display(grid)
    move(grid,input('>>').upper())
    
    
def generate_grid(size = 4):
  rows = [[Cell() for _ in range(size)] for _ in range(size)]
  for row_index,row in enumerate(rows):
    for col_index,cell in enumerate(row):
      if col_index < size - 1:
        cell.right = row[col_index + 1]
      if col_index > 0:
        cell.left = row[col_index - 1]
      if row_index < size - 1:
        cell.down = rows[row_index + 1][col_index]
      if row_index > 0:
        cell.up = rows[row_index - 1][col_index]
  return rows

def get_input():
  while True:
    usr_input = input('Enter Direction: ')
    if usr_input.lower() in list("wsad"):
      return VALID_DIRECTIONS[list("wsad").index(usr_input.lower())]
    elif usr_input.upper() in VALID_DIRECTIONS:
      return usr_input.upper()



def display(grid):
  output = ''
  
  for row in grid:
    for num in row:
      if not num:
        output += ' '
      else:
        output += f'{num.value} '
    output += '\n'

  print(output)

def reset_merged_status(grid):
  for row in grid:
    for cell in row:
      cell.merged = False

def randomly_place(grid, size=size):
  placed = False
  while not placed:
    random_cell = [random.randint(0,size-1),random.randint(0,size-1)]
    if not grid[random_cell[0]][random_cell[1]].value:
      grid[random_cell[0]][random_cell[1]].value = 2
      placed = True
  
def move(grid,direction):
  if direction in VALID_DIRECTIONS:
    if direction == 'UP':
      u_move(grid)
    elif direction == 'RIGHT':
      r_move(grid)
    elif direction == 'DOWN':
      d_move(grid)
    else:
      l_move(grid)
  else:
    move(grid,input('>>').upper())

def r_move(grid):
  for cell_start in grid[0]:
    cell = cell_start
    while cell and cell.value:
      while cell.can_move_into ('right'):
        if cell.value == cell.right.value:
          cell.right.value += cell.value
          cell.value = 0
          cell.right.merged = True
          cell = cell.right
          print('merge right')
        elif cell.right.value == 0:
          cell.right.value = cell.value
          cell.right.merged = cell.merged
          cell.merged = False
          cell.value = 0
          cell = cell.right
          print('move right')
        pass
      cell = cell_start.down

def l_move(grid):
  for cell_start in reversed(grid[0]):
    cell = cell_start
    while cell and cell.value:
      while cell.can_move_into ('left'):
        if cell.value == cell.left.value:
          cell.left.value += cell.value
          cell.value = 0
          cell.left.merged = True
          cell = cell.left
          print('merge left')
        elif cell.left.value == 0:
          cell.left.value = cell.value
          cell.left.merged = cell.merged
          cell.merged = False
          cell.value = 0
          cell = cell.left
          print('move left')
        pass
      cell = cell_start.down

def u_move(grid):
  for row in grid:
    cell_start = row[0]
    cell = cell_start
    while cell and cell.value:
      while cell.can_move_into('up'):
        if cell.value == cell.up.value:
          cell.up.value += cell.value
          cell.value = 0
          cell.up.merged = True
          cell = cell.up
          print('merge up')
        elif cell.up.value == 0:
          cell.up.value = cell.value
          cell.up.merged = cell.merged
          cell.value = 0
          cell.merged = False
          cell = cell.up
          print('move up')
      cell = cell_start.right

def d_move(grid):
  for row in reversed(grid):
    cell_start = row[0]
    cell = cell_start
    while cell and cell.value:
      while cell.can_move_into('down'):
        if cell.value == cell.down.value:
          cell.down.value += cell.value
          cell.value = 0
          cell.down.merged = True
          cell = cell.down
          print('merge up')
        elif cell.down.value == 0:
          cell.down.value = cell.value
          cell.down.merged = cell.merged
          cell.value = 0
          cell.merged = False
          cell = cell.down
          print('move down')
      cell = cell_start.right




if __name__ == '__main__':
  main()
