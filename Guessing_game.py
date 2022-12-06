# You need three functions in order to create this game.
#You need a shuffle function
#You need a guess function
#You need a check the guess function

# mylist = [' ', '0', ' ']

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    
    
def guess_game():
    guess = ''
    while guess not in ['1 ','0','2 ']
        guess = input('Pick the number: 0,1 or 2')
    return int(guess)
    
def check_guess(mylist,guess):
    if mylist[guess] == 0:
        print('Correct')
    else:
        print('wrong guess')
        print(mylist)
        
        
#Intital List

mylist = [' ', '0', ' ']

#Shuffle list

mixedup_list = shuffle_list(mylist)

#User guess

guess = guess_game()

#Check guess

check_guess(mixedup_list, guess)
    
 
