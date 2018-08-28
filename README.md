# Hello World!
Welcome to my little "Vegan Cookbook".

Visit my live website here:
https://vegan-cookbook.herokuapp.com/


## Getting Started

**YAYAY**




Thank you for visiting my site!
**Hope you enjoy the cookbook!**

Best wishes,

Annie



# Hello Developers / Coders / Techies!
Welcome to my little "Vegan Cookbook" 

Visit my live website [here](https://EXAMPLE.herokuapp.com/)


### Pseudo Code

First Load:
- landing page
- three cards 'breakfast', 'main course', 'dessert'





## Technologies Used
- Python 3.4.3
- Flask 1.0.2
- PyMongo 3.7.1
- MongoDB
- Flask-PyMongo 2.0.1
- Bootstrap 4.1.2 (with dependecies jQuery 3.3.1 and popper 1.14.3)
- MaterializeCSS version 0.100.2 
- my own CSS
- Flask Jinja templates mixed with HTML5



## Testing
- Created a series of unit tests in `tests.py` which initially failed. 
- These tests made a range of assertions which can be seen in the comments of each test in that file.
- Once a full range of tests were created, I then created `utils.py` with utility functions that related to each test.
- These functions are explained in the comments within `utils.py`
- When the functions were complete, all tests were then correctly passing, and I ensured they continued to pass while developing further code.


## Manual Testing

- used Developer Tools in browser to test smaller view-ports and mobile responsiveness
- Try to create a new recipe and enter an empty username, see that an error is shown
- Try to create a new recipe and enter a taken username, see that an error is shown
- Try to create a new recipe and enter a valid username, see that the new recipe is saved with the new author name
- Try to create a new recipe and click on the Author drop down button, find the newly added author



## Known Limitations/Issues

- Users are not able to upload images on (new) receipe creation - since MongoDB is a document-oriented database, there is no way to store image files in MongoDB
- because there is no user authentication and verification, I decided to not make a edit/delete Author button available for my users
- Using CSS3 animations not displayed on older browsers (although they aren't important to the functionality of the game)



Thank you for visiting my site!

**Hope you enjoy the cookbook!**

Best wishes,

Annie
