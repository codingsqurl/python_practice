import random                                                                                
# test

# this stays together because it starts getting a secret number and tells you all at once    
# later in the code will ask what you think the number is                   
secret_number = random.randint(1, 10)                                       
print("im thinking of a number between 1 and 10")
print("Type: i give up , if you dont want to try anymore...")

def main():
    attempts = 0
# this is the actual game loop
# starting the loop
    while True:

    # this is where you check to see if the user is ready or the user wants to give up
        user_input = input("take a guess..")
        if user_input.lower().strip() == "im ready":
            continue
        if user_input.lower().strip() == "i give up":
            print("dont feel bad it could just be broken code.. i gupted it!!")
            break
# the try handles validation
        try:
# Reads the users input and turns it in to an integer 
            guess = int(user_input)
        except ValueError:
# incase of the user typing anythin other than a whole number
            print("Oops!, Thats not a valid number! Try typing a WHOLE number...")
            continue
        attempts += 1
 

# first the code will sort through each of the conditions underneath until one is 
# suitable for what the user has entered

        if guess < secret_number:
            print("Too low, try again!") #for if the user is too low 
        elif guess > secret_number:
            print("Too high, try again!") # for if the user is too high

        else:   
            print("🎉Good job bro!🎉 im proud of your intuitive mastery!🧙🏼‍♂️") # for if the user guesses the answer correctly
            print(f"it took you {attempts} trys to guess correctly")
            break # so the program will stop when the user has sucessfully guessed the answer
                                           
if __name__ == "__main__":
    main()
