# Wat er nog bij moet
# Eerst 'Rolling...' weergeven en dan de dobbelsteen
# Klikken op de dobbelsteen zorgt dat er opnieuw wordt gegooid


from random import randint
import time

number = randint(1,4)

'''
dit is niet nodig om het te laten werken, daarom staat het nu als comment

def roll_number():
  print('Rolling...')
  time.sleep(0.5)
  print(number)

roll_number() 
'''

def draw_die():
    if number == 1:
        rect(25,25,50,50)
        fill(0)
        ellipse(50,50,10,10)
    elif number == 2:
        rect(25,25,50,50)
        fill(0)
        ellipse(35,35,10,10)
        ellipse(65,65,10,10)
    elif number == 3:
        rect(25,25,50,50)
        fill(0)
        ellipse(50,50,10,10)
        ellipse(35,35,10,10)
        ellipse(65,65,10,10)
    elif number == 4:
        rect(25,25,50,50)
        fill(0)
        ellipse(35,35,10,10)
        ellipse(35,65,10,10)
        ellipse(65,35,10,10)
        ellipse(65,65,10,10)

draw_die()

'''
turn = 0
global_turn = 0
players = (number of players)

if turn % players == 0:
    global_turn += 1
'''
