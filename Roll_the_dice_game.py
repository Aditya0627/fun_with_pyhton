import random
x,y= 0,0
min = 1
max = 6

def run_the_game():

    roll_dice = input('Guess your numbers and after guessing enter "yes" or "y" or enter "n" or "no"\n')
    x= input('enter the number you have guessed ->')
    y = input('enter the number you have guessed ->')

    global run
    if roll_dice == 'yes' or roll_dice == 'y':
         run = True

    else:
         run = False

run_the_game()
base   = '+-------+         +-------+'
sep    = '         '
blank  = '|       |'
left   = '| *     |'
middle = '|   *   |'
right  = '|     * |'
both   = '| *   * |'

dice = [(blank, middle, blank),
        (left,  blank,  right),
        (left,  middle, right),
        (both,  blank,  both ),
        (both,  middle, both ),
        (both,  both,   both )]

def print_dice(a,b):
    print(base)
    print('\n'.join(a + sep + b for a, b in zip(dice[a-1], dice[b-1])))
    print(base)

while (run):

    print('rolling the dices........wait!')
    print('the values are.....')
    c = (str((random.randint(min, max))))
    d = (str((random.randint(min, max))))
    c = int(c)
    d = int(d)
    print_dice(c,d)
    if c == x and d == y:
        print("bullseye....!")
        run_the_game()
    else:
        print('Try your luck again')
        run_the_game()


