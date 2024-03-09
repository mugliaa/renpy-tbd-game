# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

init python:
    class recipe:
        def __init__(self, name, ingredients):
            self.name = name
            self.ingredients = ingredients

    # Static Variables
    store.recipes = []
    store.recipes.append(recipe('Recipe1', ['Ingredient1', 'Ingredient2', 'Ingredient3']))

    # Dynamic Variables
    store.mixed_items = []
    store.mixed_items_size = 0
    store.mixing_complete = False
    store.matching_recipe = None

    def reset_store():
        store.mixed_items = []
        store.mixed_items_size = 0
        store.mixing_complete = False
        store.matching_recipe = None

label start:

    $ reset_store()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    e "You've created a new Ren'Py game."

    scene shelves2

    "We need to organize! There are [store.mixed_items_size] items in the container."

    while not store.mixing_complete:
        call screen dragndrop

    "Completed: [store.mixed_items]"

    "Matching Recipe: [store.matching_recipe]"

    # This ends the game.

    return
