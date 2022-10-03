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
            print("\nThe stranger walks away, smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #passes the 3 variables to the score()



if __name__ == "__main__":
    start()
