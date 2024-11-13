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
            if result != "Lost":

                # Level 2

                result2 = ""

                print("This is Level 2")

                words2 = {1: "liberty",2: "recommend",3: "guideline",4: "prohibited",5: "pharoah"}

                j_words2 = {1: "ytiberl",2: "omrcendme",3: "eglidnuei",4: "ipthorbide",5: "oahphr"}
                for i in j_words2:

                    n = 2

                    while n > 0:
                        print("Your word is:", j_words2[i])

                        guess = input("Enter your guessed word:")

                        if words2[i] == guess:
                            print("Bravo!")
                            break

                        else:
                            n -= 1

                            if n == 0:
                                print("Incorrect! you have lost the game.")
                                result2 += "Lost"
                                exit()
                            elif n == 1:
                                print("Try Again")
                                continue
                            break

            else:
                exit()
                if result2 != "Lost":

                    # Level 3

                    print("This is Level 3")

                    words3 = {1: "psychology",2: "demonstrate",3: "pneumonia",4: "homogeneous",5: "conscience"}

                    j_words3 = {1: "yglopysoho",2: "omrdtneaest",3: "uenonpima",4: "esemoohgnoue",5: "sncceionse"}

                    for i in j_words3:

                        n = 2

                        while n > 0:

                            print("Your word is:", j_words3[i])

                            guess = input("Enter your guessed word:")

                            if words3[i] == guess:
                                print("Bravo!")
                                break

                            else:
                                n -= 1

                                if n == 0:
                                    print("Incorrect! you have lost the game.")
                                    exit()

                                elif n == 1:
                                    print("Try Again")
                                    continue
                                break
