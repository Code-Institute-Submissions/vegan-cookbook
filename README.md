# Hello World!
Welcome to my little "Vegan Cookbook" 

Visit my live website [here](https://vegan-cookbook.herokuapp.com/)

TODO:
unittest
validation rule on fields
flash messages to inform user (success, fail)
Move "New Author" to the top of "Add Author"





## Technologies Used
- [Python 3.4.3] (https://docs.python.org/3.4/tutorial/)
- [Flask 1.0.2] (http://flask.pocoo.org/)
- [PyMongo 3.7.1] (https://api.mongodb.com/python/current/)
- [MongoDB] (https://www.mongodb.com/what-is-mongodb)
- [Flask-PyMongo 2.0.1] (https://flask-pymongo.readthedocs.io/en/latest/)
- [Bootstrap 4.1.2] (https://getbootstrap.com/docs/4.1/getting-started/introduction/) 
- with dependecies jQuery 3.3.1 and popper 1.14.3
- [MaterializeCSS version 0.100.2] (http://archives.materializecss.com/0.100.2/)
- CSS
- HTML5 
- JavaScript



# Testing (TODO: re-do ) Test on own code/logic!
- Created a simple unit test in `tests.py` which initially failed. 
- These tests made a range of assertions which can be seen in the comments of each test in that file.
- Once a full range of tests were created, I then created `utils.py` with utility functions that related to each test.
- These functions are explained in the comments within `utils.py`
- When the functions were complete, all tests were then correctly passing, and I ensured they continued to pass while developing further code.


## Testing Procedure

### Manual Testing (TODO re-do)

- used Developer Tools in browser to test smaller view-ports and mobile responsiveness
- Try to create a new recipe and select an existing Author Name
- Try to create a new recipe and select and created a new Author Name
- Try to created a new Author Name 
- Try to create a new recipe 
- Try to edit/update an existing recipe 
- Try to delete an existing recipe 


## Known Limitations/Issues (TODO re-do)

- Users are not able to upload their own images on (new) receipe creation - since MongoDB is a document-oriented database, there is no way to store image files in MongoDB
- because there is no user authentication and verification, I decided to not make a edit/delete Author button available for my users
- Using CSS3 animations not displayed on older browsers (although they aren't important to the functionality of the game)


### UX Design

First Load:
- landing page
- three cards 'breakfast', 'main course', 'dessert'



Thank you for visiting my site!

**Hope you enjoy the cookbook!**

Best wishes,

Annie
