# Drag-n-Drop

init python:

    def check_recipe_match():
        for recipe in store.recipes:
            if (store.mixed_items[0][0] == recipe.ingredients[0] and store.mixed_items[1][0] == recipe.ingredients[1] and store.mixed_items[2][0] == recipe.ingredients[2]):
                return recipe.name

        return None

    def handle_drag(drag, drop):
        if not drop:
            return

        # Add the dragged item and its container to the list
        store.mixed_items.append((drag[0].drag_name, drop.drag_name))
        store.mixed_items_size = store.mixed_items_size + 1
        store.mixing_complete = store.mixed_items_size == 3

        if store.mixing_complete:
            store.matching_recipe = check_recipe_match()

        return True

screen dragndrop:

    draggroup:

        # The container.
        drag:
            drag_name "Container"
            draggable False
            xpos 1500 ypos 1250

            add "container"

        # The ingredients.
        drag:
            drag_name "Ingredient1"
            droppable False
            dragged handle_drag
            xpos 500 ypos 210

            add "ingredient"

        drag:
            drag_name "Ingredient2"
            droppable False
            dragged handle_drag
            xpos 1000 ypos 210

            add "ingredient"

        drag:
            drag_name "Ingredient3"
            droppable False
            dragged handle_drag
            xpos 1500 ypos 210

            add "ingredient"

        drag:
            drag_name "Ingredient4"
            droppable False
            dragged handle_drag
            xpos 2000 ypos 210

            add "ingredient"

        drag:
            drag_name "Ingredient5"
            droppable False
            dragged handle_drag
            xpos 2500 ypos 210

            add "ingredient"

        drag:
            drag_name "Ingredient6"
            droppable False
            dragged handle_drag
            xpos 3000 ypos 210

            add "ingredient"
