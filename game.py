#---------IMPORTS--------#
from time import sleep as delay
import random

class WordModel:
    def __init__(self,word,hint,hint2) -> None:
        self.word = word
        self.firstHint = hint
        self.secondHint = hint2

word1 = WordModel('WALK','Walk in the streets', 'You do this when get out of your house')
word2 = WordModel('COMPUTER', 'Make math calcs fast', 'Bill Gates loves it ')
word3 = WordModel('SMARTPHONE', 'Almost everyone have one', 'Steve Jobs was the first man made this')
word4 = WordModel('SPORT', 'Atlethic do this', 'Everyone must do')

word_array = [word1,word2,word3]

#----------GAME VARIABLES---------#

print("""
__        _____ _______        __
\ \      / /_ _|_   _\ \      / /
 \ \ /\ / / | |  | |  \ \ /\ / / 
  \ V  V /  | |  | |   \ V  V /  
   \_/\_/  |___| |_|    \_/\_/   
            MINI-GAME
""")

word_selected = random.choice(word_array)
player_name = str(input("What's your name, player? ").capitalize())

delay(1)

start = str(input('Type ENTER to start, {}'.format(player_name)))
print('='*50)

delay(2)

print('Alright, {}, your word have {} letters'.format(player_name,len(word_selected.word)))
print('You can call a hint typing "hint". You have two hints remains')
print('')

#========PLAYER AREA========#

hint_counter = 2 # number of hint per question
chances = 3 # number of trys
letters_remains = len(word_selected.word) # length of letters in selected word
letters_discovered = [] # This array will prevane user reutilize the same letter 

while chances > 0:
    player_input = str(input('Type a letter (or call hint): ').upper())
    print('='*50)

    if player_input in letters_discovered:
        print('You already find this letter. Try other')
        print('')
    
    elif player_input in word_selected.word and player_input != '':
        letters_remains = letters_remains - 1
        letters_discovered += player_input

        print('YEAH! The letter {} have in word'.format(player_input))
        print('have {} letters remain'.format(letters_remains))
        
        print('')
        
        print(letters_discovered)
    
    elif player_input == 'HINT':
        
        if hint_counter == 2:
            
            print('Alright, your hint is: \n {}'.format(word_selected.firstHint))
            print('')
            
            hint_counter = hint_counter - 1
        
        elif hint_counter == 1:
            
            print('Alright, your hint is: \n {}'.format(word_selected.secondHint))
            print('')
            
            hint_counter = hint_counter - 1
        
        else:
            print("You don't have more hints. Sorry.")
            print('')
    
    else:
        print("The letter {} don't exist in word. You lost one chance".format(player_input))
        
        chances = chances - 1

        print('You have {} tries'.format(chances))
    
    if letters_remains == 0:
        print(' \n ')
        break
print(' ')
#win_color = '\033[32m'
#lose_color = '\033[31m'

if chances == 0:
    delay(1)
    print('\033[31mYou lose :(\033[m \nThe word was \033[1m{}\033[m'.format(word_selected.word))
else:
    delay(1)
    print('\033[32mYou win!\033[m\nThe word is \033[1m{}\033'.format(word_selected.word))