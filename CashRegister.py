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
price = 10.03


# What if we had a limited supply of coins in our til?
totalQuartersInTill = 75
totalDimesInTill = 25
totalNickelsInTill = 20
totalPenniesInTill = 100


def num_coins(cash, price):
    
    if cash < price:
        print("You don't have enough money for this trasaction")
        return
    
    totalInTill = (totalQuartersInTill *0.25) + (totalDimesInTill *0.10) + (totalNickelsInTill *0.05) + (totalPenniesInTill * 0.01)
    change = round(cash - price, 2)

    if totalInTill < change:
        print("I'm sorry but I can't make that much change... Would you like to use debit or credit instead?")
        return


    #coins
    q = 0.25
    d = 0.10
    n = 0.05
    p = 0.01

    print("Thank you for your business, your change is: $" + str(change))
    dimes = 0
    quarters = 0
    nickels = 0
    pennies = 0
    
    # quarters
    quartersToGive = change / q
    
    if quartersToGive > totalQuartersInTill:
        changeLeft = change - totalQuartersInTill * q
        quarters = totalQuartersInTill * q
        print("I don't have enough quarters, I will have to give you smaller change, I'm sorry.")
    else:
        quarters = quartersToGive * q
        changeLeft = change - quarters


    #dimes
    if changeLeft >= d:
        dimesToGive = changeLeft / d
        if dimesToGive > totalDimesInTill:
            changeLeft = change - totalDimesInTill * d
            dimes = totalDimesInTill * d
            print("I don't have enough Dimes, I will have to give you smaller change, I'm sorry.")
        else:
            dimes = dimesToGive * d
            changeLeft = changeLeft - dimes

    #nickels
    if changeLeft >= n:
        nickelsToGive = changeLeft / n
        if nickelsToGive > totalNickelsInTill:
            changeLeft = change - totalNickelsInTill * n
            dimes = totalNickelsInTill * n
            print("I don't have enough nickels, I will have to give you smaller change, I'm sorry.")
        else:
            nickels = nickelsToGiveRounded * n
            changeLeft = changeLeft - nickels

    #pennies
    if changeLeft >= p:
        penniesToGive = changeLeft / p
        pennies = penniesToGive * p
        changeLeft = changeLeft - pennies

    
    print("gave " + str(int(quarters / q)) + " quarters")
    print("gave " + str(int(dimes / d)) + " dimes")
    print("gave " + str(int(nickels / n)) + " nickels")
    print("gave " + str(int(pennies / p)) + " pennies")
    print("for a total of " + str(int(quarters + dimes + nickels + pennies)) + " coins")

    if changeLeft <= 0:
        print("Thanks, and have a nice day.  =D")
    else:
        print("uh oh, something went wrong!")
        print("change left: " + str(changeLeft))
    return  

num_coins(cash, price)


