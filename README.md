# Task Manager app using Flask and MongoDB

Mini Project - Wal Through

# putting everything in place
sudo pip3 install Flask

sudo pip3 install flask_pymongo



# CDN - add styling
https://materializecss.com/
https://cdnjs.com/libraries/jquery
https://google.github.io/material-design-icons/

# IMPORTANT
materializecss.com provides different versions of their code examples!
I'm using the base_lms.html because it contains the right CND version which
runs the retrospective version of all Forms, Buttons and Icons.
base_lms.html  && addtask.html


# on app.py
# The use of request.form
request.form.get() 

request.form.get('category_name') 

Or like this:

request.form['category_name'] 

These two things are basically identical.
The only difference is that with:
request.form.get('category_name')
You can supply a second argument to the get function which becomes the 
'default' value if the dictionary (in this case request.form is a dictionary) 
doesn't contain the first argument.