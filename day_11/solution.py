def test():
  monkey_0 = [79,98]
  monkey_1 = [54, 65, 75, 74]
  monkey_2 = [79, 60, 97]
  monkey_3 = [74]
  counter_0 = 0
  counter_1 = 0
  counter_2 = 0
  counter_3 = 0

  for i in range(20):
    print("Monkey 0:", monkey_0)
    print("Monkey 1:", monkey_1)
    print("Monkey 2:", monkey_2)
    print("Monkey 3:", monkey_3)
    print()
    for j in range(len(monkey_0)):
      new_num = monkey_0[j]*19
      new_num = new_num // 3
      counter_0 += 1
      if new_num%23==0:
        monkey_2.append(new_num)
      else:
        monkey_3.append(new_num)
    monkey_0 = []
    
    for j in range(len(monkey_1)):
      new_num = monkey_1[j]+6
      new_num = new_num // 3
      counter_1 += 1
      if new_num%19==0:
        monkey_2.append(new_num)
      else:
        monkey_0.append(new_num)
    monkey_1 = []
    
    for j in range(len(monkey_2)):
      new_num = monkey_2[j]*monkey_2[j]
      new_num = new_num // 3
      counter_2 += 1
      if new_num%13==0:
        monkey_1.append(new_num)
      else:
        monkey_3.append(new_num)
    monkey_2 = []
    
    for j in range(len(monkey_3)):
      new_num = monkey_3[j] + 3
      new_num = new_num // 3
      counter_3 += 1
      if new_num % 17 == 0:
        monkey_0.append(new_num)
      else:
        monkey_1.append(new_num)
    monkey_3 = []

  return [counter_0, counter_1, counter_2, counter_3]

def prob1():
  monkey_0 = [56, 56, 92, 65, 71, 61, 79]
  monkey_1 = [61, 85]
  monkey_2 = [54, 96, 82, 78, 69]
  monkey_3 = [57, 59, 65, 95]
  monkey_4 = [62, 67, 80]
  monkey_5 = [91]
  monkey_6 = [79, 83, 64, 52, 77, 56, 63, 92]
  monkey_7 = [50, 97, 76, 96, 80, 56]
  
  
  
  counter_0 = 0
  counter_1 = 0
  counter_2 = 0
  counter_3 = 0
  counter_4 = 0
  counter_5 = 0
  counter_6 = 0
  counter_7 = 0
  for i in range(20):
    
    for j in range(len(monkey_0)):
      new_num = monkey_0[j]*7
      new_num = new_num // 3
      counter_0 += 1
      if new_num%3==0:
        monkey_3.append(new_num)
      else:
        monkey_7.append(new_num)
    monkey_0 = []
    
    for j in range(len(monkey_1)):
      new_num = monkey_1[j]+5
      new_num = new_num // 3
      counter_1 += 1
      if new_num%11==0:
        monkey_6.append(new_num)
      else:
        monkey_4.append(new_num)
    monkey_1 = []
    
    for j in range(len(monkey_2)):
      new_num = monkey_2[j]*monkey_2[j]
      new_num = new_num // 3
      counter_2 += 1
      if new_num%7==0:
        monkey_0.append(new_num)
      else:
        monkey_7.append(new_num)
    monkey_2 = []
    
    for j in range(len(monkey_3)):
      new_num = monkey_3[j] + 4
      new_num = new_num // 3
      counter_3 += 1
      if new_num % 2 == 0:
        monkey_5.append(new_num)
      else:
        monkey_1.append(new_num)
    monkey_3 = []
    
    for j in range(len(monkey_4)):
      new_num = monkey_4[j]*17
      new_num = new_num // 3
      counter_4 += 1
      if new_num%19==0:
        monkey_2.append(new_num)
      else:
        monkey_6.append(new_num)
    monkey_4 = []
    
    for j in range(len(monkey_5)):
      new_num = monkey_5[j] + 7
      new_num = new_num // 3
      counter_5 += 1
      if new_num % 5 == 0:
        monkey_1.append(new_num)
      else:
        monkey_4.append(new_num)
    monkey_5 = []
    
    for j in range(len(monkey_6)):
      new_num = monkey_6[j] + 6
      new_num = new_num // 3
      counter_6 += 1
      if new_num % 17 == 0:
        monkey_2.append(new_num)
      else:
        monkey_0.append(new_num)
    monkey_6 = []
    
    for j in range(len(monkey_7)):
      new_num = monkey_7[j] + 3
      new_num = new_num // 3
      counter_7 += 1
      if new_num % 13 == 0:
        monkey_3.append(new_num)
      else:
        monkey_5.append(new_num)
    monkey_7 = []

  to_return = [counter_0, counter_1, counter_2, counter_3, counter_4, counter_5, counter_6, counter_7]
  to_return.sort()
  print(to_return)
  return to_return[-1]*to_return[-2]


def prob2():
  monkey_0 = [56, 56, 92, 65, 71, 61, 79]
  monkey_1 = [61, 85]
  monkey_2 = [54, 96, 82, 78, 69]
  monkey_3 = [57, 59, 65, 95]
  monkey_4 = [62, 67, 80]
  monkey_5 = [91]
  monkey_6 = [79, 83, 64, 52, 77, 56, 63, 92]
  monkey_7 = [50, 97, 76, 96, 80, 56]

  counter_0 = 0
  counter_1 = 0
  counter_2 = 0
  counter_3 = 0
  counter_4 = 0
  counter_5 = 0
  counter_6 = 0
  counter_7 = 0

  mod = 3*11*7*2*19*5*17*13


  for i in range(10000):
    for j in range(len(monkey_0)):
      new_num = monkey_0[j]*7
      new_num = new_num%mod
      if new_num%3==0:
        monkey_3.append(new_num)
      else:
        monkey_7.append(new_num)
    counter_0 += len(monkey_0)
    monkey_0 = []

    for j in range(len(monkey_1)):
      new_num = monkey_1[j]+5
      new_num = new_num%mod
      if new_num%11==0:
        monkey_6.append(new_num)
      else:
        monkey_4.append(new_num)
    counter_1 += len(monkey_1)
    monkey_1 = []

    for j in range(len(monkey_2)):
      new_num = monkey_2[j]*monkey_2[j]
      new_num = new_num%mod
      if new_num%7==0:
        monkey_0.append(new_num)
      else:
        monkey_7.append(new_num)
    counter_2 += len(monkey_2)
    monkey_2 = []

    for j in range(len(monkey_3)):
        new_num = monkey_3[j] + 4
        new_num = new_num%mod
        if new_num % 2 == 0:
            monkey_5.append(new_num)
        else:
            monkey_1.append(new_num)
    counter_3 += len(monkey_3)
    monkey_3 = []

    for j in range(len(monkey_4)):
      new_num = monkey_4[j]*17
      new_num = new_num%mod
      
      if new_num%19==0:
        monkey_2.append(new_num)
      else:
        monkey_6.append(new_num)
    counter_4 += len(monkey_4)
    monkey_4 = []

    for j in range(len(monkey_5)):
      new_num = monkey_5[j] + 7
      new_num = new_num%mod
      if new_num % 5 == 0:
        monkey_1.append(new_num)
      else:
        monkey_4.append(new_num)
    
    counter_5 += len(monkey_5)
    monkey_5 = []

    for j in range(len(monkey_6)):
      new_num = monkey_6[j] + 6
      new_num = new_num%mod
      
      if new_num % 17 == 0:
        monkey_2.append(new_num)
      else:
        monkey_0.append(new_num)
    counter_6 += len(monkey_6)
    monkey_6 = []

    for j in range(len(monkey_7)):
      new_num = monkey_7[j] + 3
      new_num = new_num%mod
      if new_num % 13 == 0:
        monkey_3.append(new_num)
      else:
        monkey_5.append(new_num)
    counter_7 += len(monkey_7)
    monkey_7 = []

  to_return = [counter_0, counter_1, counter_2, counter_3, counter_4, counter_5, counter_6, counter_7]
  to_return.sort()
  print(to_return)
  return to_return[-1]*to_return[-2]


print(prob1())
print(prob2())