# calculate the change to give from a transaction in a cash register
# useable coins: 
# quarter (25)
# dime (10)
# nickel (5)
# penny (1)
# return the number of coins it would take to make change
# want to use biggest coins first 

# Transaction
cash = 20
price = 10.47

# What if we had a limited supply of coins in our til?
totalQuartersInTill = 75
totalDimesInTill = 25
totalNickelsInTill = 20
totalPenniesInTill = 100

def num_coins(cash, price):
    
    # Validation
    if cash < price:
        print("You don't have enough money for this trasaction")
        return
    
    totalInTill = (totalQuartersInTill *0.25) + (totalDimesInTill *0.10) + (totalNickelsInTill *0.05) + (totalPenniesInTill * 0.01)
    change = round(cash - price, 2)

    if totalInTill < change:
        print("I'm sorry but I can't make that much change... Would you like to use debit or credit instead?")
        return

    print("Thank you for your business, your change is: $" + str(change))

    #coins
    q = 0.25
    d = 0.10
    n = 0.05
    p = 0.01

    # local vars
    dimes = 0
    quarters = 0
    nickels = 0
    pennies = 0
    quartersToGive = 0
    dimesToGive = 0
    nickelsToGive = 0
    penniesToGive = 0
    
    # quarters
    quartersToGive = int(change / q)
    print(str(quartersToGive) + "fuck me")
    if quartersToGive > totalQuartersInTill:
        changeLeft = round(change - totalQuartersInTill * q, 2)
        quarters = totalQuartersInTill * q
        print("I don't have enough quarters, I will have to give you smaller change, I'm sorry.")
    else:
        quarters = quartersToGive * q
        changeLeft = round(change - quarters, 2)
        print("change left after quarters: " + str(changeLeft))


    #dimes
    if changeLeft >= d:
        dimesToGive = int(changeLeft / d)
        if dimesToGive > totalDimesInTill:
            changeLeft = round(change - totalDimesInTill * d, 2)
            dimes = totalDimesInTill * d
            print("I don't have enough Dimes, I will have to give you smaller change, I'm sorry.")
        else:
            dimes = dimesToGive * d
            changeLeft = round(changeLeft - dimes, 2)

    #nickels
    if changeLeft >= n:
        nickelsToGive = int(changeLeft / n)
        if nickelsToGive > totalNickelsInTill:
            changeLeft = round(change - totalNickelsInTill * n, 2)
            dimes = totalNickelsInTill * n
            print("I don't have enough nickels, I will have to give you smaller change, I'm sorry.")
        else:
            nickels = nickelsToGiveRounded * n
            changeLeft = round(changeLeft - nickels, 2)

    #pennies
    if changeLeft >= p:
        penniesToGive = changeLeft / p
        pennies = penniesToGive * p
        changeLeft = round(changeLeft - pennies, 2)

    
    print("gave " + str(int(quartersToGive)) + " quarters")
    print("gave " + str(int(dimesToGive)) + " dimes")
    print("gave " + str(int(nickelsToGive)) + " nickels")
    print("gave " + str(int(penniesToGive)) + " pennies")
    print("for a total of " + str(int(quartersToGive + dimesToGive + nickelsToGive + penniesToGive)) + " coins")

    if changeLeft <= 0:
        print("Thanks, and have a nice day.  =D")
    else:
        print("uh oh, something went wrong!")
        print("change left: " + str(changeLeft))
    return  

num_coins(cash, price)


