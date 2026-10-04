#Exercise 1
word= input('Enter a word')
rev_word= word[::-1]

print (rev_word)
if word == rev_word:
    print ('it is a palindrome')
else:
    print('not a palindrome')

#Exercise 2
word = input("Kindly enter a sentence: ")

print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
print("Title case:", word.title())
print("Length:", len(word))
print("Replaced 'a' with '@':", word.replace("a", "@"))
print("Split into words:", word.split())
print("Strip whitespace:", word.strip())
print("Starts with 'The':", word.startswith("The"))
print("Find 'is':", word.find("is"))
print("split string into list:", word.split())

first_word = word.split()[0]
print("First word:", first_word)

name = "Apostle"
age = 19
print(f"My name is {name} and I am {age} years old.")

#Exercise 3
#Exercise 3 - Hangman

secret_word = "EhimsMichael"
guessed_letters = ""
attempts_left = 6

print("Welcome to Hangman!")
print("The word has", len(secret_word), "letters.")

while attempts_left > 0:
    display_word = ""
    for letter in secret_word:
        if letter.lower() in guessed_letters:
            display_word = display_word + letter
        else:
            display_word = display_word + "_"

    print("\nWord:", display_word)

    if display_word == secret_word:
        print("You guessed it! The word was:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word.lower():
        guessed_letters = guessed_letters + guess
        print("Correct!")
    else:
        guessed_letters = guessed_letters + guess
        attempts_left = attempts_left - 1
        print("Wrong! Attempts left:", attempts_left)

if attempts_left == 0 and display_word != secret_word:
    print("\nGame over! The word was:", secret_word)