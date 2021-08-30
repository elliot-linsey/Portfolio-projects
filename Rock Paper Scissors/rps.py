import numpy as np 
import sys

def lst_reset():
  lst_reset.lst = ['r', 'p', 's']

lst_reset.lst = ['r', 'p', 's']

def u_choice():
  ch = input('What is your choice? ')
  if ch == 'exit':
    sys.exit('Goodbye!')
  elif ch not in lst_reset.lst:
    print('Not a valid choice!')
    return u_choice()
  return ch

def c_choice():
  ch = np.random.choice(lst_reset.lst)
  return ch

def rps():
 lst_reset()
 if rps.u_count == 5:
   return 'You win!'
 elif rps.c_count == 5:
   return 'You lose!'
 u_ch = u_choice()
 c_ch = c_choice()
 print(f'Computer choice: {c_ch}')
 if u_ch == c_ch:
   print('You drew!')
   print(f'User score = {rps.u_count}')
   print(f'Computer score = {rps.c_count}')
   return rps()
 elif u_ch == 'r' and c_ch == 's':
   rps.u_count += 1
   print(f'User score = {rps.u_count}')
   print(f'Computer score = {rps.c_count}')
   return rps()
 elif u_ch == 'r' and c_ch == 'p':
   rps.c_count += 1
   print(f'User score = {rps.u_count}')
   print(f'Computer score = {rps.c_count}')
   return rps()
 elif u_ch == 's' and c_ch == 'p':
   rps.u_count += 1
   print(f'User score = {rps.u_count}')
   print(f'Computer score = {rps.c_count}')
   return rps()
 elif u_ch == 's' and c_ch == 'r':
   rps.c_count += 1
   print(f'User score = {rps.u_count}')
   print(f'Computer score = {rps.c_count}')
   return rps()
 elif u_ch == 'p' and c_ch == 'r':
   rps.u_count += 1
   print(f'User score = {rps.u_count}')
   print(f'Computer score = {rps.c_count}')
   return rps()
 elif u_ch == 'p' and c_ch == 's':
   rps.c_count += 1
   print(f'User score = {rps.u_count}')
   print(f'Computer score = {rps.c_count}')
   return rps()

rps.u_count = 0
rps.c_count = 0

print(rps())