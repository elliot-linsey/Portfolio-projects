import numpy as np

num = np.random.randint(1,101)

def choose():
  choice = input('What is your choice? ')
  choose.count += 1
  return choice
choose.count = 0
def too_low(choice, num): 
  if num - choice in range(1,11):
    print('You are low by between 1 and 10 away!')
    return number_game()
  elif num - choice in range(11,21):
    print('You are low by between 11 and 20 away!')
    return number_game()
  elif num - choice in range(21,31):
    print('You are low by between 21 and 30 away!')
    return number_game()
  elif num - choice in range(31,41):
    print('You are low by between 31 and 40 away!')
    return number_game()
  elif num - choice in range(41,51):
    print('You are low by between 41 and 50 away!')
    return number_game()
  elif num - choice in range(51,61):
    print('You are low by between 51 and 60 away!')
    return number_game()
  elif num - choice in range(61,71):
    print('You are low by between 61 and 70 away!')
    return number_game()
  elif num - choice in range(71,81):
    print('You are low by between 71 and 80 away!')
    return number_game()
  elif num - choice in range(81,91):
    print('You are low by between 81 and 90 away!')
    return number_game()
  elif num - choice in range(91,100):
    print('You are low by between 91 and 99 away!')
    return number_game()
  

def too_high(choice, num):  
  if choice - num in range(1,11):
    print('You are high by between 1 and 10 away!')
    return number_game()
  elif choice - num in range(11,21):
    print('You are high by between 11 and 20 away!')
    return number_game()
  elif choice - num in range(21,31):
    print('You are high by between 21 and 30 away!')
    return number_game()
  elif choice - num in range(31,41):
    print('You are high by between 31 and 40 away!')
    return number_game()
  elif choice - num in range(41,51):
    print('You are high by between 41 and 50 away!')
    return number_game()
  elif choice - num in range(51,61):
    print('You are high by between 51 and 60 away!')
    return number_game()
  elif choice - num in range(61,71):
    print('You are high by between 61 and 70 away!')
    return number_game()
  elif choice - num in range(71,81):
    print('You are high by between 71 and 80 away!')
    return number_game()
  elif choice - num in range(81,91):
    print('You are high by between 81 and 90 away!')
    return number_game()
  elif choice - num in range(91,100):
    print('You are high by between 91 and 99 away!')
    return number_game()


def number_game():
  #print(num)
  choice = choose()
  try:
    choice = int(choice)
    if choice == num: 
      return(str(f'You win! You used {choose.count} attempts!'))
    elif choice < 0:
      print('Only positive numbers!')
      return number_game()
    elif choice > 100:
      print('Too high!')
      return number_game()
    elif choice < num:
      return too_low(choice, num)
    elif choice > num: 
      return too_high(choice, num)
  except: #If they input a symbol like '@' which cannot be converted to integer
    print('Only integers!')
    return number_game()
  
print(number_game())



