def prob_1(path):
  gas = open(path,"r")
  gas = gas.read()
  gas = gas.rstrip("\n")
  gas_counter = 0
  #>>> < < > < > > < < < > > < > > ><<<>>><<<><<<>><>><<>>

  already_landed = set([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)])
  for i in range(2022):
    highest_y = 0
    for item in already_landed:
      if item[1] > highest_y:
        highest_y = item[1]
    if i % 5 == 0:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((4,4+highest_y))
      set_of_moving_points.add((5,4+highest_y))
      most_left = 2
      most_right = 5
      
    elif i % 5 == 1:
      set_of_moving_points = set()
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((2,5+highest_y))
      set_of_moving_points.add((3,5+highest_y))
      set_of_moving_points.add((4,5+highest_y))
      set_of_moving_points.add((3,6+highest_y))
      most_left = 2
      most_right = 4
      
    elif i % 5 == 2:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((4,4+highest_y))
      set_of_moving_points.add((4,5+highest_y))
      set_of_moving_points.add((4,6+highest_y))
      most_left = 2
      most_right = 4
  
    elif i % 5 == 3:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((2,5+highest_y))
      set_of_moving_points.add((2,6+highest_y))
      set_of_moving_points.add((2,7+highest_y))
      most_left = 2
      most_right = 2
      
    elif i % 5 == 4:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((2,5+highest_y))
      set_of_moving_points.add((3,5+highest_y))
      most_left = 2
      most_right = 3

    
    while True:
      dir = gas[gas_counter%len(gas)]
      if dir == ">":
        gas_counter += 1
        if most_right == 6:
          pass
          
        else:
          potential_set_of_moving_points = set()
          has_collision = False
          
          for tetris in set_of_moving_points:
            new_tetris = (tetris[0]+1, tetris[1])
            
            if new_tetris in already_landed:
              has_collision = True
              break
              
            else:
              potential_set_of_moving_points.add(new_tetris)
              
          if has_collision == False:
            set_of_moving_points = potential_set_of_moving_points
            most_right += 1
            most_left += 1
      elif dir == "<":
        gas_counter += 1
        if most_left == 0:
          pass
          
        else:
          potential_set_of_moving_points = set()
          has_collision = False
          
          for tetris in set_of_moving_points:
            new_tetris = (tetris[0]-1, tetris[1])
            
            if new_tetris in already_landed:
              has_collision = True
              break
              
            else:
              potential_set_of_moving_points.add(new_tetris)
              
          if has_collision == False:
            set_of_moving_points = potential_set_of_moving_points
            most_left -= 1
            most_right -= 1
            
      has_landed = False
      where_to_move = set()
      
      for tetris in set_of_moving_points:
        new_tetris = (tetris[0], tetris[1]-1)
        
        if new_tetris in already_landed:
          has_landed = True
          break
          
        else:
          where_to_move.add(new_tetris)
      
      if has_landed == False:
        set_of_moving_points = where_to_move
        
      if has_landed == True: 
        for item in set_of_moving_points:
          already_landed.add(item)
        break
  returned_y = 0
  for item in already_landed:
    if item[1] > returned_y:
      returned_y = item[1]
  return returned_y

def prob_2(path):
  gas = open(path,"r")
  gas = gas.read()
  gas = gas.rstrip("\n")
  gas_counter = 0
  already_landed = set([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)])
  def already_seen_pattern(visited):
    highest_y = 0
    for (x,y) in visited:
      if y > highest_y:
        highest_y = y
    new_list = []
    for (x,y) in visited:
      if highest_y - y <= 1000:
        new_list.append((x,highest_y - y))
    return frozenset(new_list)

  hash_map = {}
  high = 0
  counter = 0
  added = 0
  while counter<1000000000000:
    highest_y = max([y for (x,y) in already_landed])
    if counter % 5 == 0:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((4,4+highest_y))
      set_of_moving_points.add((5,4+highest_y))
      most_left = 2
      most_right = 5
      
    elif counter % 5 == 1:
      set_of_moving_points = set()
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((2,5+highest_y))
      set_of_moving_points.add((3,5+highest_y))
      set_of_moving_points.add((4,5+highest_y))
      set_of_moving_points.add((3,6+highest_y))
      most_left = 2
      most_right = 4
      
    elif counter % 5 == 2:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((4,4+highest_y))
      set_of_moving_points.add((4,5+highest_y))
      set_of_moving_points.add((4,6+highest_y))
      most_left = 2
      most_right = 4
  
    elif counter % 5 == 3:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((2,5+highest_y))
      set_of_moving_points.add((2,6+highest_y))
      set_of_moving_points.add((2,7+highest_y))
      most_left = 2
      most_right = 2
      
    elif counter % 5 == 4:
      set_of_moving_points = set()
      set_of_moving_points.add((2,4+highest_y))
      set_of_moving_points.add((3,4+highest_y))
      set_of_moving_points.add((2,5+highest_y))
      set_of_moving_points.add((3,5+highest_y))
      most_left = 2
      most_right = 3

    while True:
      dir = gas[gas_counter%len(gas)]
      if dir == ">":
        gas_counter += 1
        if most_right == 6:
          pass
          
        else:
          potential_set_of_moving_points = set()
          has_collision = False
          
          for tetris in set_of_moving_points:
            new_tetris = (tetris[0]+1, tetris[1])
            
            if new_tetris in already_landed:
              has_collision = True
              break
              
            else:
              potential_set_of_moving_points.add(new_tetris)
              
          if has_collision == False:
            set_of_moving_points = potential_set_of_moving_points
            most_right += 1
            most_left += 1
      elif dir == "<":
        gas_counter += 1
        if most_left == 0:
          pass
          
        else:
          potential_set_of_moving_points = set()
          has_collision = False
          
          for tetris in set_of_moving_points:
            new_tetris = (tetris[0]-1, tetris[1])
            
            if new_tetris in already_landed:
              has_collision = True
              break
              
            else:
              potential_set_of_moving_points.add(new_tetris)
              
          if has_collision == False:
            set_of_moving_points = potential_set_of_moving_points
            most_left -= 1
            most_right -= 1
      has_landed = False
      where_to_move = set()
      
      for tetris in set_of_moving_points:
        new_tetris = (tetris[0], tetris[1]-1)
        
        if new_tetris in already_landed:
          has_landed = True
          break
          
        else:
          where_to_move.add(new_tetris)
      
      if has_landed == False:
        set_of_moving_points = where_to_move
        
      if has_landed == True: 
        for item in set_of_moving_points:
          already_landed.add(item)
        break
        high = max([y for (x,y) in already_landed])

        visit = (gas_counter, counter%5, already_seen_pattern(already_visited))
        if visit in hash_map :
          (prev_t, prev_y) = hash_map[visit]
          max_left_times = (1000000000000-counter)//(counter - prev_t)
          added += max_left_times*(high - prev_y)
          counter += max_left_times*(counter - prev_t)
        hash_map[visit] = (counter,high)
        break
    counter += 1
  return added  

print(prob_1("/Users/farishambo/Desktop/advent_git/AdventOfCode2022/day_17/input.txt"))

print(prob_2("/Users/farishambo/Desktop/advent_git/AdventOfCode2022/day_17/input.txt"))