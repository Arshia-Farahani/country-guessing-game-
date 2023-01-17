
country = input("Player 1,please name a country: ")
num = int(input('Pleas enter the number of letters of your chosen country: '))
while num < 100:
    if num == 5:
        print("Please spell it out")
        letters = (input("Letter 1: "), input("Letter 2: "), input("Letter 3: "), input("Letter 4: "), input("Letter 5: "))
        print("Player 2,you have only 5 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "___")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "__")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "_")
        if guess == letters[4]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 4 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "___")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "__")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "_")
        if guess == letters[4]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 3 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "___")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "__")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "_")
        if guess == letters[4]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 2 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "___")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "__")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "_")
        if guess == letters[4]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,last chance to guess the letter!!")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "___")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "__")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "_")
        if guess == letters[4]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4]:
            print("Your guess was Wrong!!")

        print("Player 2,you have only one chance to guess the name of the country chosen by Player 1.")
        guess = input("Player 2,please guess the country chosen by Player 1: ")

        if guess == country:
            print("=================================\nCongratulations......you Won\n=================================")
        else:
            print(
                "=================================\nUnfortunately........you lost!\n=================================")

        country = input("Player 1,please name a country: ")
        num = int(input('Pleas enter the number of letters of your chosen country: '))

    if num == 4:
        print("Please spell it out")
        letters = (input("Letter 1: "), input("Letter 2: "), input("Letter 3: "), input("Letter 4: "))
        print("Player 2,you have only 4 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "___")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "__")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "_")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 3 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "___")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "__")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "_")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3])
        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 2 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "___")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "__")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "_")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3])
        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,last chance to guess the letter!!")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print(
                "Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "___")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "__")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "_")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3])
        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only one chance to guess the name of the country chosen by Player 1.")
        guess = input("Player 2,please guess the country chosen by Player 1: ")

        if guess == country:
            print("=================================\nCongratulations......you Won\n=================================")
        else:
            print(
                "=================================\nUnfortunately........you lost!\n=================================")

        country = input("Player 1,please name a country: ")
        num = int(input('Pleas enter the number of letters of your chosen country: '))

    if num == 3:
        print("Please spell it out")
        letters = (input("Letter 1: "), input("Letter 2: "), input("Letter 3: "))
        print("Player 2,you have only 3 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "__")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "_")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2])

        if guess != letters[0] and guess != letters[1] and guess != letters[2]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 2 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "__")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "_")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2])

        if guess != letters[0] and guess != letters[1] and guess != letters[2]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,last chance to guess the letter!!")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "__")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "_")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2])

        if guess != letters[0] and guess != letters[1] and guess != letters[2]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only one chance to guess the name of the country chosen by Player 1.")
        guess = input("Player 2,please guess the country chosen by Player 1: ")

        if guess == country:
            print("=================================\nCongratulations......you Won\n=================================")
        else:
            print(
                "=================================\nUnfortunately........you lost!\n=================================")

        country = input("Player 1,please name a country: ")
        num = int(input('Pleas enter the number of letters of your chosen country: '))

    if num == 2:
        print("Please spell it out")
        letters = (input("Letter 1: "), input("Letter 2: "))
        print("Player 2,you have only 2 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "_")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1])

        if guess != letters[0] and guess != letters[1]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,last chance to guess the letter!!")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[0] + "_")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1])

        if guess != letters[0] and guess != letters[1]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only one chance to guess the name of the country chosen by Player 1.")
        guess = input("Player 2,please guess the country chosen by Player 1: ")

        if guess == country:
            print("=================================\nCongratulations......you Won\n=================================")
        else:
            print(
                "=================================\nUnfortunately........you lost!\n=================================")

        country = input("Player 1,please name a country: ")
        num = int(input('Pleas enter the number of letters of your chosen country: '))

    if num == 6:
        print("Please spell it out")
        letters = (
        input("Letter 1: "), input("Letter 2: "), input("Letter 3: "), input("Letter 4: "), input("Letter 5: "),
        input("Letter 6: "))
        print("Player 2,you have only 6 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[
                0] + "_____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "____")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "___")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "__")
        if guess == letters[4]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[
                4] + "_")
        if guess == letters[5]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_____" + letters[
                4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4] and guess != letters[5]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 5 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[
                0] + "_____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "____")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "___")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "__")
        if guess == letters[4]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[
                4] + "_")
        if guess == letters[5]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_____" + letters[
                4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4] and guess != letters[5]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 4 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[
                0] + "_____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "____")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "___")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "__")
        if guess == letters[4]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[
                4] + "_")
        if guess == letters[5]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_____" + letters[
                4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4] and guess != letters[5]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 3 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[
                0] + "_____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "____")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "___")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "__")
        if guess == letters[4]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[
                4] + "_")
        if guess == letters[5]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_____" + letters[
                4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4] and guess != letters[5]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only 2 chances to guess.")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[
                0] + "_____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "____")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "___")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "__")
        if guess == letters[4]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[
                4] + "_")
        if guess == letters[5]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_____" + letters[
                4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4] and guess != letters[5]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,last chance to guess the letter!!")
        guess = input("Player 2,please guess one of the letters of the country chosen by Player 1: ")

        if guess == letters[0]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + letters[
                0] + "_____")
        if guess == letters[1]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_" + letters[
                1] + "____")
        if guess == letters[2]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "__" + letters[
                2] + "___")
        if guess == letters[3]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "___" + letters[
                3] + "__")
        if guess == letters[4]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "____" + letters[
                4] + "_")
        if guess == letters[5]:
            print("Good job. Your guess was right! " + "\nThe place of this letter in the word is " + "_____" + letters[
                4])

        if guess != letters[0] and guess != letters[1] and guess != letters[2] and guess != letters[3] and guess != \
                letters[4] and guess != letters[5]:
            print("Your guess was Wrong!!\nPlease try again.")

        print("Player 2,you have only one chance to guess the name of the country chosen by Player 1.")
        guess = input("Player 2,please guess the country chosen by Player 1: ")

        if guess == country:
            print("=================================\nCongratulations......you Won\n=================================")
        else:
            print(
                "=================================\nUnfortunately........you lost!\n=================================")

        country = input("Player 1,please name a country: ")
        num = int(input('Pleas enter the number of letters of your chosen country: '))
