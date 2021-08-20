import random

def rpsls_game(user_input):

  rpsls = ['rock', 'paper', 'scissor', 'lizard', 'spock']

  cpu_choice = random.choice([cpu for cpu in rpsls])

  win, lost, tie = 'won', 'lost', 'tie'

  if (user_input==rpsls[0]):
    if (cpu_choice==rpsls[2]) or (cpu_choice==rpsls[3]):
      print(f'CPU\'s choice: {cpu_choice} \n You {win} the game')
    if (cpu_choice==rpsls[1]) or (cpu_choice==rpsls[4]):
      print(f'CPU\'s choice: {cpu_choice} \n You {lost} the game')

  if (user_input==rpsls[1]):
    if (cpu_choice==rpsls[0]) or (cpu_choice==rpsls[4]):
      print(f'CPU\'s choice: {cpu_choice} \n You {win} the game')
    if (cpu_choice==rpsls[3]) or (cpu_choice==rpsls[2]):
      print(f'CPU\'s choice: {cpu_choice} \n  You {lost} the game')


  if (user_input==rpsls[2]):
    if (cpu_choice==rpsls[1]) or (cpu_choice==rpsls[3]):
      print(f'CPU\'s choice: {cpu_choice} \n You {win} the game')
    if (cpu_choice==rpsls[0]) or (cpu_choice==rpsls[4]):
      print(f'CPU\'s choice: {cpu_choice} \n You {lost} the game')


  if (user_input==rpsls[3]):
    if (cpu_choice==rpsls[4]) or (cpu_choice==rpsls[1]):
      print(f'CPU\'s choice: {cpu_choice}\n You {win} the game')
    if (cpu_choice==rpsls[0]) or (cpu_choice==rpsls[2]):
      print(f'CPU\'s choice: {cpu_choice} \n You {lost} the game')

  if (user_input==rpsls[4]):
    if (cpu_choice==rpsls[2]) or (cpu_choice==rpsls[0]):
      print(f'CPU\'s choice: {cpu_choice} \n You {win} the game')
    if (cpu_choice==rpsls[1]) or (cpu_choice==rpsls[3]):
      print(f'CPU\'s choice: {cpu_choice} \n You {lost} the game')

  if user_input == cpu_choice:
    print(f"CPU\'s choice: {cpu_choice} It's {tie}!!")

if __name__ == '__main__':
  user_input = str(input("Choose Rock, Paper, Scissor, Lizard, Spock: "))
  user_input = user_input.lower()
  rpsls_game(user_input)
