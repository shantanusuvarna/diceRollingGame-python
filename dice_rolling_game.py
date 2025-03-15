import random

#Loop
# Ask: roll the dice?
i=int(1)
die = 5
while True:
    choice = input ('Roll the dice? (y/n):').lower()
    choice2 = int(input('No.of Dice? (1-5):'))
    
# If user enters y
    while choice2 <=die:
        if choice == 'y':

            if i <=4:
            
                die1 = random.randint(1,6)      #Generates random integer
                print(f'{die1}')
                print('Dice roll count:', int(i))   
                i = i+1

            elif i >=4:

                print("No more chances")
        
    
        elif choice == 'n':

            print('Thanks for playing!')
            break


        else:
            print('Invalid Choice')
#     Generate two numbers
#     Print them
# If user enter n
#     Print thank you message
#     Terminate
# Else
#     Print invalid choice
