
import random





def my_func():
    x = input('Type rock, paper or scissors:')
    rps = ['Rock','Paper','Scissors']
    computer_action= random.choice(rps)
    user_action = x.capitalize()
    if user_action in rps:
        if user_action == computer_action : 
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "Rock":
            if computer_action == "Scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "Paper":
            if computer_action == "Rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "Scissors":
            if computer_action == "Paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
    else:
        print('Oops, something went wrong! Maybe you misspelled it.')

if __name__=='__main__':
    my_func()
    
