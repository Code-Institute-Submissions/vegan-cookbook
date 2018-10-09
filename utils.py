import json

def check_recipename(recipe_name):
    '''
    If a Recipe Name was left empty 
    then it is invalid 
    '''
    if recipe_name == "":
        return False
    return True

