# Scrambled word game

words = {1: "calendar",2: "dictionary",3: "atmosphere",4: "temperature",5: "laboratory"}

j_words = {1: "daelnrac",2: "troinoadiory",3: "htapseomre",4: "eatrptumere",5: "aaltrorbyo"}

# Level 1

print("This is Level 1")
result = ""

for i in j_words:
    n = 2

    while n > 0:
        print("Your word is:", j_words[i])

        guess = input("Enter your guessed word: ")

        if words[i] == guess:
            print("Bravo!")
            break

        else:
            n -= 1

            if n == 0:
                print("Incorrect! you have lost the game.")
                result += "Lost"
                exit()

            elif n == 1:
                print("Try Again")
                continue
            break
