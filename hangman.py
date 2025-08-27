import random
import string

# -------------------------------
# Word list (you can expand it)
# -------------------------------
WORDS = [
    "python", "java", "kotlin", "swift", "programming", "computer",
    "hangman", "algorithm", "machine", "learning", "artificial",
    "intelligence", "variable", "function", "developer"
]

# -------------------------------
# AI Helper (letter frequency based)
# -------------------------------
LETTER_FREQUENCY = "etaoinshrdlcumwfgypbvkjxqz"  # common → rare

def ai_suggest(used_letters):
    """Suggest next best letter not already guessed."""
    for letter in LETTER_FREQUENCY:
        if letter not in used_letters:
            return letter
    return None

# -------------------------------
# Main Hangman Game
# -------------------------------
def hangman():
    word = random.choice(WORDS).lower()
    word_letters = set(word)     # letters in word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()         # guessed letters
    lives = 7

    print("🎮 Welcome to Hangman with AI Helper!")
    print("I (the AI) will try to help you guess the word.")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Used letters:", " ".join(sorted(used_letters)))

        # Show current word progress
        word_progress = [letter if letter in used_letters else "_" for letter in word]
        print("Word:", " ".join(word_progress))

        # AI Suggestion
        suggestion = ai_suggest(used_letters)
        print("🤖 AI suggests trying:", suggestion.upper())

        # Player input
        user_letter = input("Your guess (or press Enter to use AI suggestion): ").lower()

        if user_letter == "":
            user_letter = suggestion  # accept AI's choice

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"✅ Good guess! {user_letter} is in the word.")
            else:
                lives -= 1
                print(f"❌ Wrong guess! {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print("⚠️ You already guessed that letter.")
        else:
            print("❌ Invalid input. Try again.")

    # End game
    if lives == 0:
        print(f"\n💀 You lost! The word was: {word.upper()}")
    else:
        print(f"\n🎉 Congrats! You guessed the word: {word.upper()}")

# -------------------------------
# Run game
# -------------------------------
if __name__ == "__main__":
    hangman()
