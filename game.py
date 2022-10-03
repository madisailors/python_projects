# 
# Python: 3.10.7
#
# Author: Madi Sailors
#
# Purpose: Tech Academy Python course, demonstrating how to pass variables
#          from function to function while producing a functional game
#          
#           function_name(variable)  means that we pass in the variable
#           return variable means we are returning the variable back to
#           calling the function


def start(nice=0,mean=0,name=""):
    #get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        checks if this is a new game or not, if so,
        gets users name, if not, thank user for playing
        and continue w/ game
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several people. \nYou can choose to be nice or mean")
                    print("\nbut at the end of the game your fate will be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\A stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
            print("\nThe stranger gives you $20 and walks away, smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #passes the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({} nice) and ({} mean).".format(name,nice,mean)) 

def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2:
        win(nice,mean,name)
    if mean> 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you won! \n And you're rich! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name) #calling our again function and pass in our vairables


def lose(nice,mean,name):
    #substitute the {} wildcards w variable values
    print("\nAaah, too bad, game over {}! \nYou live in a dirty beat up van \nby the river, wrecthed and alone!".format(name))
    again(nice,mean,name)
    

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh no, so sad, sorry to see you go bestie!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for yes or ( N ) for no: \n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #not resetting name variable bc user has decided to play again
    start(nice,mean,name)





if __name__ == "__main__":
    start()
