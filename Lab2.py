# Jerico Lozares - Lab 2

def getACard() :
    """ returns one random interger from 1-13 """
    from random import randint
    import random
    num = random.randint(1, 13)
    return num

def showCard(num) :
    """ Converts the card number to a printable value 
        Argument: a random integer from 1-13
        Return: a printable card value
    """
    if num == 1 :
        card = 'A'
    elif num == 11 :
        card = 'J'
    elif num == 12 :
        card = 'Q'
    elif num == 13 :
        card = 'K'
    else :
        card = num 
    return card

def updateTotal(num, total) :
    """ Updates the total of one player 
        Argument: a random integer from 1-13 and the current total of a player
        Return: updated total of a player 
    """
    if (num in {1, 11, 12, 13}):
        num = 10
    newTotal = total + num
    return newTotal

def oneGame() :
    """ plays one game by calling the previous 3 functions and coordinating them """
    firstCompVal = getACard()
    compTotal = updateTotal(firstCompVal, total = 0)
    secondCompVal = getACard()
    compTotal = updateTotal(secondCompVal, compTotal)
    firstUserVal = getACard()
    userTotal = updateTotal(firstUserVal, total = 0)
    secondUserVal = getACard()
    userTotal = updateTotal(secondUserVal, userTotal)
    print("My cards:", showCard(firstCompVal), "and ?")
    print("Your cards:", showCard(firstUserVal), "and", showCard(secondUserVal))
    choice = input("One more card? y/n: ")
    if choice not in ('y', 'n') :
        choice = input("One more card? y/n: ")
    while choice == 'y' :
        thirdUserVal = getACard()
        print("Your card:", showCard(thirdUserVal))
        userTotal = updateTotal(thirdUserVal, userTotal)
        if userTotal > 21 :
            print("I won!")
            print("Your total is", userTotal)
            return
        elif userTotal == 21 :
            print("You won!")
            print("Your total is", userTotal)
            return
        else :
            choice = input("One more card? y/n: ")
    while compTotal < 17 :
        nextCompVal = getACard()
        print("My card is:", showCard(nextCompVal))
        compTotal = updateTotal(nextCompVal, compTotal)
        if compTotal == 21 :
            print("I won!")
            print("Your total is", userTotal)
        elif compTotal > 21 :
                print("You won!")
        else :
            if compTotal <= userTotal :
                print("You won!")
            else :
                print("I won!")
            print("Your total:", userTotal)
            print("My total:", compTotal)
    '''if compTotal >= 17 :
        if compTotal <= userTotal :
            print("You won!")
        else :
            print("I won!")
        print("Your total:", userTotal)
        print("My total:", compTotal)'''

def main() :
    oneGame()
    print("Play another game? y/n:")
    answer = input()
    while answer == 'y' : 
        oneGame()
        print("Play another game? y/n:")
        answer = input()
    if answer != 'y' :
        return 0

main()




