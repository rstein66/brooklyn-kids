# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ollie = Character("Ollie", color="#c8ffc8")
define kit = Character("Kit", color="#c8c8ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene tunnel

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show otter

    ollie "Hi, I'm Ollie the Otter! Welcome to my home, the Brooklyn Children's Museum! What's your name?"

    show kidback

    kit "Wooh! You can talk?! That's so cool! I'm Kit! Do you really live here?!"
    ollie "It's! Awesome, right?!"

    # This ends the game.

    return
