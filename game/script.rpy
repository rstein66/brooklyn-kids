# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ollie = Character("Ollie")
define kit = Character("Kit")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bcmTunnel

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.


    kit "Wait up, ollie!"
    kit "ollie!"
    kit "I said wait up!"
    kit "...ollie?"
    ollie "Boo!"
    kit "Yikes... not again."
    kit "Are you scared?"
    kit "Not at all."
    kit "Running off like that is dangerous, you know."
    kit "We are in the forest. We could get lost."
    ollie "Okay okay mom. I won't do it again."

    # This ends the game.

    return
