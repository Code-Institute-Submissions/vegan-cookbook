# Hello World!
Welcome to my little "Vegan Cookbook".

Visit my live website here:
https://annies-cookbook.herokuapp.com/


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

- Ensure initial page load is correct, with list of hiscores shown
- Try entering an empty username, see that an error is shown
- Try entering a taken username from hiscore list, see that an error is shown
- Try entering a valid username, see that the game progresses to the first riddle and that username is shown in page header with 0 score
- Answer first riddle with blank answer, see error message and 1 retry
- Answer first riddle with incorrect answer, see error message and no retry, and that game moves to next riddle
- Answer second riddle with correct answer, see success message, next riddle loaded, and score in page header is incremented by 1
- Try loading homepage again at this point, see that you are redirected back to the start of the riddle game with same username, score reset to 0
- Complete game, see that all riddles in json file are asked, answering questions with variations on casing (upper case, lower case, etc.), 
- Checked if score increments successfully with each correct answer,
- Checked if game successfully redirects to '/gameover' after last riddle
- On gameover, see that success message is displayed, that score and username are added to hiscores list
- After gameover, try to load /riddles, see that session has been cleared and new username input is required, redirected to homepage


## Known Limitations/Issues

- Player can hit refresh after getting correct answer and get awarded more points - could be solved by tracking whether user has already played this riddle or not.
- Method of writing hiscores to a file is vulnerable to problems where two users write to that file at the same time, and one of their changes are lost. 
- No way of re-using your old username to play another game
- Players can go directly to gameover at any point by adding '/gameover' to the URL, which clears their session and stores their score
- Using CSS3 animations not displayed on older browsers (although they aren't important to the functionality of the game)



Thank you for visiting my site!

**Hope you enjoy the cookbook!**

Best wishes,

Annie
