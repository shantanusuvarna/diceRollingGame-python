Dice Rolling Game



Overview

This is a simple dice rolling game that allows users to roll a dice a limited number of times. The user can choose to roll the dice multiple times, and the program will generate random dice rolls for each turn. The number of dice to roll can be selected by the user, and the program will handle invalid inputs and end when the user chooses to stop or exhausts their chances.



Features

The user can decide whether to roll the dice or not.
The user can specify how many dice they want to roll (up to a limit of 5).
The dice roll will generate random values between 1 and 6.
The game ends after 4 rolls, or when the user chooses to stop.


How to Play

The game prompts the user to choose whether they want to roll the dice or not.
If the user chooses to roll, they are then asked how many dice they want to roll (from 1 to 5).
The program generates random dice rolls and displays the results.
The user can continue rolling or stop at any time.
The game terminates when the user chooses not to roll or after 4 rolls.


Instructions

Start the program by running the Python script.
You will be asked:
"Roll the dice? (y/n)" to decide if you want to roll.
"No.of Dice? (1-5)" to choose how many dice you'd like to roll (up to 5).
The program will generate random dice rolls for each roll and display them along with the count of rolls.
The program will stop either when you roll 4 times or choose to stop by entering 'n'.


Example:

Roll the dice? (y/n): y
No.of Dice? (1-5): 2
4
Dice roll count: 1

Roll the dice? (y/n): y
No.of Dice? (1-5): 3
6
Dice roll count: 2

Roll the dice? (y/n): n
Thanks for playing!


Code Explanation
random.randint(1,6) is used to generate random numbers between 1 and 6, simulating the roll of a die.
The while loop checks if the user wants to continue rolling or not, and restricts the number of rolls to 4.
The input for the number of dice ensures that the user selects between 1 and 5 dice to roll.
If the user enters an invalid choice for either rolling or the number of dice, the program will prompt them again.


