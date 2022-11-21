 import random
#This is our list of words
lists = ["trend", "stung", "witch", "games", "phone", "bring", "throw", "rifts", "adult", "beach"]
#These functions chose a random word and makes it a list so we can use it #in our game.
random = random.randint(0,9)
word = lists[random]
# This will list our word so we can compare individual letters. word_list = list(word)
#These variables are global so they can be changed globally. letters = "trend"
words = "trend"
#Our function "game" is our code that will actually do all of the work.
"""
Within this function, the user will be asked to input a word. If this word is
more or less than five letters, then the code will recognize that and tell the
user to only input a word that is five letters. Once the user inputs a word that
is five letters, the code is check to see if the word inputted matches the word
that was randomly chosen before the function began. If the words match, it would stop the game and say "Correct", while if the words did not match, it would tell the user to try again and continue with the game. The next portion of the code compares each letter of the inputted word, to every letter of the original
word. If there are any letters that are the same, it gets added to a list that
will be printed at the end of the loop. After the comparison is done, the code goes on to compare the letters in a specific spot, for example, the letter that
is in the first place of both the original word and the inputted word are compared to see if they are the same. If they are the same, that letter is
added to a list that will be printed at the end of the loop, and that same value, or letter is removed from the other list. By removing this value from the other list, it makes sure that only values that are not in their correct places are in that list, and the values that are in the correct places are in the other list.
The last part of a singular loop, is to print these two lists. The first list
that is printed is the list that tells that user which values, or letters, are in
the correct place. The second list that is printed tells the user which letters

 are not in the correct place. After those two lists are printed, the code will loop back up to the top and repeat the process five more time, or until the user guesses the word.
"""
# My partner created this function for our program. def word_length():
# These global variables allow me to use them in any part of the code. global words, letters, length
# These functions will get the word from the user and turn it into a list. words = input("Take your guess! ")
letters = list(words)
# This will take the list of letters and get how many letters there are in the word. length = len(letters)
#If the word is not exactly five letters, the user will recieve an error message. if length != 5:
while length != 5:
print("ONLY ENTER A FIVE LETTER WORD! ")
#The user gets to enter a word until they enter a word that is five letters. words = input("Take your guess! ")
letters = list(words)
length = len(letters)
def game():
for i in range(1):
print("Welcome to Codle! Enter a five letter word to try and guess the randomized word. We reccomend using a pen a paper to help solve the word!")
print(" ")
for i in range(6):
# My partner created this portion of our program.
word_length()
#This sees if the word inputted matches the original word exactly. The code will stop if
they match.
if words == word:
print("Correct!") break

 else:
print("Try again!")
# This is the end of the portionmy partner created of our program.
#These variables call the individual letters of the inputted word. input_z = letters[0]
input_o = letters[1]
input_t =letters[2]
input_r = letters[3] input_f = letters[4]
#This will create an empty list. We are able to add to this list if it matches a certain criteria.
my_letters = []
"""
This part of the code takes a specific letter from the inputted word and compares it to each letter in the original word. If there is a letter that is in both the original and inputted word, the place of the letter will be added the empty list. There are 5 comparisons, one for each letter of the inputted word.
"""
for i, letter in enumerate(word_list):
if letter == input_z: my_letters.append("First")
for i, letter in enumerate(word_list): if letter == input_o:
my_letters.append("Second") for i, letter in enumerate(word_list):
if letter == input_t: my_letters.append("Third")
for i, letter in enumerate(word_list): if letter == input_r:
my_letters.append("Fourth") for i, letter in enumerate(word_list):
if letter == input_f: my_letters.append("Fifth")
# This empty list allows us to put in values so we can use them later on in the game. my_list = []

 """
These five functions will check to see if the letters in a specific place are the same. The variables made are assigned to specific letters for both the original and the inputted word. The code will compare the first letter of the original word to the first letter of the inputted word. If they are the same, that place will be added to the correct list and that place will then be taken off of the list
for the incorrect places. This function repeats five times and compares each place to the saame place in the other word.
"""
original_z = word_list[0]
if original_z == input_z:
my_list.append("First ") my_letters.remove("First")
original_o = word_list[1] if original_o == input_o:
my_list.append("Second ") my_letters.remove("Second")
original_t = word_list[2] if original_t == input_t:
my_list.append("Third ") my_letters.remove("Third")
original_r = word_list[3] if original_r == input_r:
my_list.append("Fourth ") my_letters.remove("Fourth")
original_f = word_list[4] if original_f == input_f:
my_list.append("Fifth ") my_letters.remove("Fifth")
#These two functions will print both lists made above.
#They will tell the user if the letters inputted are in the right or wrong spots.
# My partner made this portion of our code.

 print("These letters are in the correct place: " + str(my_list)) print("These letters are NOT in the correct place: " + str(my_letters)) # This is the end of the portion my partner made of our code.
print(" ") """
This last line of code will print after the user either guesses the word, or after the user runs out of tries to guess the word. The original word will be printed in both instances, and will thank the user for playing the game.
"""
print("The word was: " + str(word) + ". Thank you for playing!")
game()
