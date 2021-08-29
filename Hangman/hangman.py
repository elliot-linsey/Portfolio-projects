import numpy as np

def word_choice():
  lst = ['paris', 'london', 'rome', 'sydney', 'kingston', 'dubai', 'tokyo', 'milan', 'budapest']
  choice = np.random.choice(lst)
  choice_list = []
  for x in choice:
    choice_list.append(x)
  return choice_list

prev_ch = []
choice = word_choice()
empty_lst = ['_']*len(choice)

def word_input():
  ch = input('What is your choice? ')
  if ch not in choice:
    prev_ch.append(ch)
    word_input.count -= 1
  elif ch in choice:
      word_input.count += 0
  return ch

word_input.count = 10

def hangman():
  #print(choice)
  print(f'Previous choices: {prev_ch}')
  print(empty_lst)
  if empty_lst == choice:
    return 'You win!'
  elif word_input.count == 0:
    print(f'The answer was {choice}')
    return 'You lose!'
  print(f'{word_input.count} guesses left!')
  choose = word_input()
  indexes = []
  if empty_lst != choice:
    for i in range(len(choice)):
      if choice[i] == choose:
        indexes.append(i)
        for x in indexes:
          empty_lst[x] = choose
    return hangman()
  
print(hangman())