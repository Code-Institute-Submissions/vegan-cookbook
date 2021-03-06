import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# from utils import ###


app = Flask(__name__, static_url_path='/static')
app.config["MONGO_DBNAME"] = 'anniescookbook'
app.config["MONGO_URI"] = 'mongodb://coffeeipsum:1Diploma1Diploma@ds225382.mlab.com:25382/anniescookbook'
#Please note - in this lession we have not learned how to use an evironemnt variable yet!


mongo = PyMongo(app)


# --------------------- Home / Landing Page ---------------------------

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", 
    recipes=mongo.db.recipes.find())



# --------------------- Recipes ---------------------------------- 

@app.route('/all_recipes')
def all_recipes():
    '''
    PAge showing all recipes in the database
    '''

    return render_template(
        "recipes.html", 
        recipes=mongo.db.recipes.find()
    )

@app.route('/view_recipe/<recipe_id>')
@app.route('/view_recipe/<recipe_id>/<created>')
def view_recipe(recipe_id=None, created=None):
    '''
    View an individual recipe by object ID.
    Upon saving the new recipe on endpoint 'add_recipe', the user will be
    redirected to this endpoint and will see a success
    message on the top of the page to inform them that the recipe
    has been submitted successfully. The 'created' parameter is only included 
    in this case.
    '''
    if recipe_id is not None:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        if created is not None:
            message = """ Thank you! You've successfully submitted your
                '%s' recipe!""" % the_recipe.get("recipe_name")
        
            return render_template("recipes.html", 
                    message=message,
                    recipes=[the_recipe]
            )
        
        return render_template("recipes.html", 
                recipes=[the_recipe]
        )


@app.route('/recipes_by_category/<category_name>')
def recipes_by_category(category_name):
    
    return render_template(
        "recipes_by_category.html", 
        recipes=mongo.db.recipes.find({"category_name": category_name}),
        categories=mongo.db.categories.find(),
        category_name=category_name.replace('_', ' ').title()
        
    )
    

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find(),
    authors=mongo.db.authors.find())
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    new_recipe = recipes.insert_one(request.form.to_dict())
    return redirect(url_for('view_recipe', recipe_id=new_recipe.inserted_id, created="created"))
    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, 
        categories=all_categories, authors=mongo.db.authors.find(), 
        recipe_id=recipe_id)
    
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'recipe_name':request.form.get('recipe_name'),
        'ingredients': request.form.get('ingredients'),
        'recipe_description': request.form.get('recipe_description'),
        'preparation_time': request.form.get('preparation_time'),
        'allergens': request.form.get('allergens'),
        'author_name': request.form.get('author_name'),
        'tags': request.form.get('tags')
    })
    return redirect(url_for('all_recipes'))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))
 
 
 
    
# --------------------- NEW : Authors ----------------------------------    

# FYI: there's no overview page with All Authors
# FYI: there's no edit button for Authors
# FYI: there's no delete button for Authors

@app.route('/add_author')
def add_author():
    return render_template('addauthor.html')    



@app.route('/insert_author', methods=['POST'])
def insert_author():
    authors = mongo.db.authors
    author_doc = {'author_name': request.form.get('author_name')}
    authors.insert_one(author_doc)
    return redirect(url_for('home'))
    


# --------------------- Categories ----------------------------------    

""" 
I replaced the Category overview with 'Home' / Landing Page
"""



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)