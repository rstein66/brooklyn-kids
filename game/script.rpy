# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ollie = Character("Ollie", color="#c8ffc8")
define kit = Character("Kit", color="#c8c8ff")


# The game starts here.

label start:

    scene tunnel

    show otter

    ollie "Hi, I'm Ollie the Otter!"
    ollie "Welcome to my home, the Brooklyn Children's Museum!"
    ollie "What's your name?"

    show kidback

    kit "Wooh! You can talk?! That's so cool!"
    kit "I'm Kit! Do you really live here?!"
    ollie "Yes! Awesome, right?!"
    kit "Yes! I want to live here too!"

    ollie "We don't have a lot of time before your dad comes back."
    ollie "Do you want to see some of my favorite places?"
    kit "Yes, please!"

    menu:
        ollie "What do you want to do first?"
        "See who's taller":
            hide otter with dissolve
            jump measure

        "Go to Oyster City":
            jump oyster_city

label measure:
    scene ottermeasure

    menu:
        ollie "Who do you think is taller?"
        "Kit":
            jump kit_is_taller_yay
        "Ollie":
            jump kit_is_taller_sad

label kit_is_taller_yay:
    scene otterkidmeasure
    kit "Me!"
    ollie "Darn."
    scene waterbackground
    jump ending

label kit_is_taller_sad:
    scene otterkidmeasure
    ollie "You 😕"
    scene waterbackground
    jump ending

label oyster_city:
    scene oystercity
    show otter
    show kidback

    ollie "Welcome to Oyster City!"
    ollie "Oysters are really cool!"
    ollie "They live with other oysters, together on reefs."
    ollie "Oyster reefs are like apartment buildings because lots and lots of animals live in them."
    ollie "Oysters also clean the water they live in. "
    jump ending

label ending:
    show otter
    show kidback
    ollie "Oh! Is that your dad?"
    ollie "I should go before he sees me."
    hide kidback
    ollie "Thanks for hanging out with me!"
    ollie "I hope to see you again soon!"
    hide otter
    show kidfront
    kit "Thanks for showing me your home!"
    kit "Bye!"

return
