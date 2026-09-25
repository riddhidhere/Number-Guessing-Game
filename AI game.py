import random

print("=== Welcome to the GKS AI Number Guessing Challenge ===")
print("🎯 I am thinking of a number between 1 and 50.")
print("⚠️ WARNING: You only have 5 LIVES to guess it correctly!")

# 1. Computer AI picks a secret number
secret_number = random.randint(1, 50)

# 2. Set the configuration for lives
max_lives = 5
attempts = 0

# 3. Game loop
while attempts < max_lives:
    guess = int(input(f"\n[Lives Left: {max_lives - attempts}] Enter your guess: "))
    attempts += 1
    
    # 4. Check if the guess is right
    if guess == secret_number:
        print(f"🎉 CONGRATULATIONS! You beat the AI and guessed the number {secret_number}!")
        print(f"📊 Total attempts used: {attempts}")
        break
    elif guess > secret_number:
        print("📉 Too High! Try a smaller number.")
    else:
        print("📈 Too Low! Try a bigger number.")

# 5. Out of lives condition check
if attempts == max_lives and guess != secret_number:
    print("\n💥 GAME OVER! You ran out of lives.")
    print(f"🤖 The AI wins! The secret number was {secret_number}. Better luck next time!")
