import random as r
import animation as a
import sqlite3 as s
con=s.connect("Hangman.db")
cur=con.cursor()
cur.execute("create table if not exists categories (category TEXT)")
cur.execute("create table if not exists words (category TEXT, word TEXT)")

# List of words for each category
fruits = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']
cars = ['ford', 'toyota', 'honda', 'chevrolet', 'bmw', 'mercedes', 'audi', 'volkswagen', 'nissan', 'subaru', 'mazda', 'hyundai', 'kia', 'volvo', 'jeep', 'tesla']

# Insert categories into the table
cur.execute("INSERT INTO categories (category) VALUES (?)", ('fruits',))
cur.execute("INSERT INTO categories (category) VALUES (?)", ('cars',))

# Insert words into the table
for fruit in fruits:
    cur.execute("INSERT INTO words (category, word) VALUES (?, ?)", ('fruits', fruit))

for car in cars:
    cur.execute("INSERT INTO words (category, word) VALUES (?, ?)", ('cars', car))

con.commit()

con.close()
# List of words to choose from
someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

# Choose a random word from the list
someWords = someWords.split()
word = someWords[r.randint(0, len(someWords)-1)]
mylen = len(word)
guessedword = ["_"] * mylen
chances = 8

# Print initial message
print(f"Start guessing the word letter by letter \n You will get {chances} tries to find the word")

# Print initial state of guessed word
for i in range(mylen):
    print(guessedword[i], end=" ")
print()

playing, guessed = True, False                                

while playing and chances != 0:
    guess = input("Enter your guess: ")
    correct, playing = False, False

    # Check if the guessed letter is correct
    for i in range(mylen):
        if guess == word[i]:
            guessedword[i] = guess
            print(guess, end=" ")
            correct = True
        else:
            print(guessedword[i], end=" ")
            playing = True

    if correct:
        print("\n\nGood Guess!")
    else:
        chances -= 1
        print(f"\n\nWrong Guess, {chances} left")
    a.hang_animation(chances)

    # Check if all letters have been guessed
    if "_" not in guessedword:
        guessed = True
        break

if guessed:
    print(f"You have successfully guessed {word}")
else:
    print(f"\n\nYou are out of Chances\n The Word was {word}")