def generate_sensors_and_beacons(path):
  sensors = set()
  beacons = set()
  f = open(path, "r")
  for line in f:
    new_line = line.rstrip("\n")
    new_line = new_line.replace(":", "")
    new_line = new_line.replace(",", "")
    line = new_line.split()
    sens_x = int(line[2][2:])
    sens_y = int(line[3][2:])
    beacon_x = int(line[-2][2:])
    beacon_y = int(line[-1][2:])
    distance = abs(sens_x - beacon_x) + abs(sens_y - beacon_y)
    sensors.add((sens_x, sens_y, distance))
    beacons.add((beacon_x, beacon_y))

  return sensors, beacons

  
S,B = generate_sensors_and_beacons("input.txt")

def is_valid(x,y,S):
    for (sens_x,sens_y,dist) in S:
        dist_xy = abs(x-sens_x) + abs(y-sens_y)
        if dist_xy <= dist:
            return False
    return True

def prob_1():
    counter = 0
    y = 200000
    for x in range(-5000000,5000000):
        if not is_valid(x,y,S) and (x,y) not in B:
            counter += 1
    return counter 



def prob_2():
    for (sens_x,sens_y,dist) in S:
        for dist_x in range(dist+2):
            dist_y = (dist+1)-dist_x
            list_of_possible_ways = [(1,1),(1,-1),(-1,1),(-1,-1)]
            for x_add,y_add in list_of_possible_ways:
                x = sens_x+(dist_x*x_add)
                y = sens_y+(dist_y*y_add)
                if is_valid(x,y,S) and 0<=x<=4000000 and 0<=y<=4000000:
                    return x*4000000 + y
                    
print(prob_1())
print(prob_2())
