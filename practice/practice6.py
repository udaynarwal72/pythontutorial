n = 18
# no. of guesses left
# no. of guesses he took
# no. of guesse he took
# game over
# ------------------------------------------------------------------------------
atmp = 18  # atmp= atempt
gn = 10   # gn=guess no.
i = 1
print("Welcome to the game designed by Uday")
while (True):
    id1 = input("Enter your id\n")
    password = input("Enter your password\n")
    if id1 == 'Uday' and password == '123':
        while(i <= atmp):
            en = int(input("Enter the guess"))

            if en > gn:
                print("Guess number:",i, "=>You guesssed high")
                i = i+1
            elif(en == gn):
                print("Guess number:",i, "=>Congrats, you guessed right")
                break
            else:
                print("Guess number:",i, "=>You guessed low")
                i = i + 1
                continue
            if i > 10:
                print("Game over")
                break
    else:
        print("You Enterd wrong details")
    continue
# ---------------------------------------------------------------------------------