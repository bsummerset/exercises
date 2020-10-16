import random
s_num = random.randint(1, 10)
guess = 0
guess_count = 0
#print(s_num)
play_again = "yes"
while play_again == "yes":

    guess,guess_count = None, 0,random.randint(1,10)

    #SAME THING
    #s_num = random.radint(1,10)
    #guess = None
    #guess_count = 0

    while guess != s_num and guess_count < 5:
        while True:
            guess_count += 1
            try:
                guess = int(input("Please guess a number?\n"))
                break
            except ValueError:
                print("You did not enter an number... you still loose a chance.")
                guess = 0
        
        if guess == s_num:
            print("Yes you win.")
        elif guess < s_num:
            print("Your number is too low, try again.")
        else:
            print("Your number is too high, try again.")
       

    if guess_count >= 5:
        print("You guess too many times. Too bad.")

    play_again = input("Do you want to play again?\n")