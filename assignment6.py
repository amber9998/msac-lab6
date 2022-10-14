# Judy Kuo
# assignment6.py
# 26SEP2022
# CISW 24
import sys

lets_play = input('Would you like to play a game? (y/n): ')

if lets_play == 'n':
        print('Thank you for playing. Good bye.')
        sys.exit()
else: 
    print("please enter y/n")
    
    
while True:
    game_choice = input('''Choose a game or quit:
                        1) Bagels
                        2) Rock, Paper, Scissors
                        3) The Game 21
                        q) to quit
                        Enter your chioce: ''')
    
    if game_choice == 'q':
        print('Thank you for playing. Good bye.')
        sys.exit()
    
    elif game_choice == '2':
        print('You chose Rock, Paper, Scissors! Have a nice game')
    
    elif game_choice == '3':
        print('You chose The Game 21! Have a nice game')
        
    elif game_choice == '1':
        print('You chose Bagels! Have a nice game')
        
    else:
        print('Oops! please enter 1, 2, 3, or q')