import os

def main():
    won = False
    word = "qwerty"
    guessed = []
    while not won:
        printWord(word, guessed);
        letter = input("Dame una letra: ")
        guessed.append(letter)

def printWord(word, guessed):
    hiden = "";
    for letter in word:
        contains = False
        for guess in guessed:
            if letter == guess:
                contains = True
        if contains:
            hiden += letter
        else:
            hiden += "_"
    os.system("clear")
    print(hiden)

if __name__ == "__main__":
    main();