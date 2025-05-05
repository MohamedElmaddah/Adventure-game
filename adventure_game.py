import time
import random

# Val
idate input function
def validate_input(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        else:
            print(f"Invalid choice. Choose from {options}.")

# Play again function
def play_again():
    return validate_input("Play again? (yes/no): ", ['yes', 'no'])

# The score variable
score = 0

def print_pause(msg):
    time.sleep(2)
    print(msg)

def play_game():
    global score
    # Virus decision
    virus_mind = random.choice([
        'GOODBYE',
        'I WILL LEAVE YOU FOR NOW BUT YOU WILL BE DELETED SOON'
    ])
    # Choices for desktop applications
    desktop_choices = ['google', 'minecraft']
    # Random choice of the password
    passwords = ['25565', '67851', '11511', '57608']

    # First messages
    print_pause("You're tired after a long day at school.")
    print_pause("One of your friends asked you to play with him.")

    # Loop for the first choice
    choice_a = validate_input("Play or read a book? ", ['play', 'read a book'])
    if choice_a == "play":
        score -= 1
        print_pause(f"Your score is {score}")
        print_pause("You opened the game")
        print_pause("After playing for a few hours")
        print_pause("a virus appeared and teleported you inside the computer")
        print_pause("You found a war between the virus and the antivirus")

        # Loop for the second choice
        choice_b = validate_input("Run or fight? ", ['run', 'fight'])
        if choice_b == "run":
            score -= 1
            print_pause(f"Your score is {score}")
            print_pause("You ran to the desktop")
            desktop_choice = random.choice(desktop_choices)
            print_pause(f"You chose to open {desktop_choice}")
            if desktop_choice == "google":
                print_pause("You explored the internet")
                print_pause("You learned how to defeat the virus")
                print_pause("Will you go and delete it?")
            else:
                print_pause("You got distracted playing Minecraft")
                print_pause("Game Over")
                return

            # The first choice in the second choice
            choice_b_2 = validate_input("Fight the virus or enjoy the internet? ", ['fight', 'enjoy the internet'])
            if choice_b_2 == "fight":
                score += 1
                print_pause(f"Your score is {score}")
                print_pause("You tried to return to your computer")
                print_pause("The virus changed your password")
                password_choice = validate_input(f"Choose one: {passwords}: ", passwords)
                if password_choice == "25565":
                    print_pause("Correct password! You entered the computer")
                    print_pause("You found the virus on the local disk C")
                    print_pause("Run a command to vanish temporarily")
                    command = validate_input("Enter the command: ", ['vanish'])
                    score += 1
                    print_pause(f"Your score is {score}")
                    print_pause("You sneaked behind the virus to Windows")
                    print_pause("You reset your computer and the virus got deleted")
                    print_pause("You logged out safely")
                    print_pause("Game Over")
                else:
                    print_pause("Wrong password. The computer shut down")
                    print_pause("Game Over")

            elif choice_b_2 == "enjoy the internet":
                score -= 1
                print_pause(f"Your score is {score}")
                print_pause("You got trapped on the internet")
                print_pause("Game Over")

        elif choice_b == "fight":
            score += 1
            print_pause(f"Your score is {score}")
            print_pause("You helped the antivirus but it got deleted")
            print_pause("The virus said it will decide to delete the OS or you")
            print_pause(f"The virus said: {virus_mind}")
            if virus_mind == "GOODBYE":
                last_words = input("The virus asked: ANY LAST WORDS? ")
                print_pause(f"You said to the virus: {last_words}")
                print_pause("Game Over")
            else:
                print_pause("The virus gave you a few seconds to live")
                last_action = validate_input("Enjoy or try to remove it? ", ['enjoy', 'try to remove it'])
                if last_action == "enjoy":
                    score -= 1
                    print_pause(f"Your score is {score}")
                    print_pause("You enjoyed the last seconds")
                    print_pause("The virus deleted everything")
                    print_pause("Game Over")
                elif last_action == "try to remove it":
                    score += 1
                    print_pause(f"Your score is {score}")
                    print_pause("You reinstalled the antivirus")
                    print_pause("You hoped it would work, and it did")
                    print_pause("You logged back to reality")
                    print_pause("Game Over")

    elif choice_a == "read a book":
        score += 1
        print_pause(f"Your score is {score}")
        print_pause("You told your friend: Sorry, but I'll read a book")
        print_pause("You read a book about cybersecurity")
        print_pause("You heard an error sound from your computer")

        # Loop for the third choice
        choice_c = validate_input("Forget or try fixing it? ", ['forget', 'try fixing it'])
        if choice_c == "forget":
            score -= 1
            print_pause(f"Your score is {score}")
            print_pause("You ignored it, but the sound stopped")
            print_pause("Your OS got deleted with your work")
            print_pause("Game Over")
        elif choice_c == "try fixing it":
            score += 1
            print_pause(f"Your score is {score}")
            print_pause("You used your knowledge from the book")
            print_pause("After hours of work, you fixed it")
            print_pause("Game Over")

    print_pause(f"Your total score is {score}")

while True:
    play_game()
    if play_again() == 'no':
        print("Thanks for playing. Goodbye!")
        break
