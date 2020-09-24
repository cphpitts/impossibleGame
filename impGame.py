def main():
    gameActive = True
    gameReady = False
    beanCount = 16

    print("Welcome to the Bean Game!")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("Rules: There are 25 beans, you and I will take turns taking out one or two beans.")
    print("Whoever takes the last bean, loses.")
    while gameReady == False:
        readyResponse = input("Are you ready to play? ").lower()
        if readyResponse == "y" or readyResponse == "yes":
            gameReady = True
        else:
            print("Invalid response")
    while gameActive:
        print("There are {} beans left.".format(beanCount))
        validResponse = False
        while validResponse == False:
            playerTake = input("Would you like to take 1 or 2? ")
            playerTake = int(playerTake)
            print("playerTake: {}".format(playerTake))
            if playerTake == 1 or playerTake == 2:
                beanCount -= playerTake
                validResponse = True
            else:
                print("Invalid response.")
        print("\nYou took {} beans.".format(playerTake))
        print("There are {} beans left.".format(beanCount))
        computerTake = 3 - playerTake
        print("I will take {} beans.".format(computerTake))
        beanCount -= computerTake
        if beanCount == 1:
            print("There's only 1 bean left. You must take it. You lose.")
            playAgain = input("\nWould you like to play again?")
            if playAgain == "y" or playAgain == "yes":
                beanCount = 25
            else:
               gameActive = False
    print("Thanks for playing.")


if __name__ == "__main__":
    main()