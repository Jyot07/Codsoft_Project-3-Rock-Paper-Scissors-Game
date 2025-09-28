
import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Rules are simple: Rock 🪨 beats Scissors ✂️, Scissors ✂️ beat Paper 📄, and Paper 📄 beats Rock 🪨.\n")

    user_score = 0
    computer_score = 0

    while True:
        # Get user input
        user_choice = input("👉 Your move (rock/paper/scissors): ").strip().lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Not a valid choice. Pick rock, paper, or scissors.\n")
            continue

        # Computer’s random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Show choices
        print(f"\n🧑 You chose: {user_choice.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")

        # Decide winner
        if user_choice == computer_choice:
            print("😐 It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("🎉 You win this round!\n")
            user_score += 1
        else:
            print("💻 Computer takes the point.\n")
            computer_score += 1

        # Show score
        print(f"📊 Scoreboard — You: {user_score} | Computer: {computer_score}\n")

        # Play again option
        play_again = input("🔁 Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\n🏁 Game Over!")
            print(f"🎯 Final Score — You: {user_score} | Computer: {computer_score}")

            if user_score > computer_score:
                print("👏 You’re the overall winner. Well played!")
            elif user_score < computer_score:
                print("🤖 Computer wins this match. Want a rematch next time?")
            else:
                print("⚖️ It’s a draw overall. Good game!")
            break


# Run the game
rock_paper_scissors()
