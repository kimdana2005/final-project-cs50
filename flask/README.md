# CS50_Final_project - Movie4Night
### Video Demo:  https://youtu.be/12irR3NhJ0E
#### Description:
This web application will help everyone with 'don`t knowning what to watch' problem. It randomly generate a movie from database and, if chosen, this film could be a particular genre.
****
# heplers.py:
We used 2 CS50's function from Finance - `apology`(in order to create flash messages) adn `login_required` (to create features which will only be available for logined users)
# app.py: 
In app.py at first we have imports of needed libraries and functions from these libraries. 
Then we have a configuration of the app and database linking.
## route / 
After we have our first route "/" which just renders a template with "generate" button via executing genres form table and passing data to Jinja
## route /register
Then we have a "/register" route which accepts both get and post methods. In function we have if statement where we make sure which of the metods function gonna process. If the method is post we make sure all data that we recieved are provided and correct, cheking if username is not taken, if the password meets the requirements and so on. After all checks we add a new user to our database and send the registered user to log in. If the method is get, we just pass the user a register form.
## route /login 
We have taken a login function from the CS50Finance so they are the same.
## route /logoute
The same as in the "/login" route.
## route /generate
In generate route we also have two metods if method get we redirect user to main page, if not we recive genre, create some variables, then we process data, filling the movies list with films ids, we check if the user watched the movie, if wathced why would we show him the movie again, if user selected genre we show him only movies with appropriate genre, and if we made all the steps and we have no movie left, that means user watched them all! And we render a congratulate page to make the user feel a bit special) Then we get some more data from the database and passing it into render for a nice generated movie page. 
## route /changepass
The "/changepass" route is the route that used to change user's password and it is almost the same as a "/register" route, except instead of username we recive an old password, and just updating db, not inserting a value to it.
## route /add_to_watched
In "/add_to_wathced" we check if the user provided his rating of corresponding movie, update user history and user rating tables and check if the user wathced 10 movies to congratulate him for opening a new feature of the site which is an add your movie to site.
## route /add_to_later
Here we have just one move to insert into user history table status that the user has this movie in watch later list.
## route /add
In "/add" route if method is get we check if the user wathched 10 movies if yes we render him an add page, if not we redirect him on main with message.
Else we validate and recieve data and add it to db.
## route /wathced
Is the route where we simply render a page with data.
## route /chat
In the las route we have a message function that accepts message from user via post method, validates the data and inserts it into the db. If the messages are to many, we delete some. Get method renders a page with a relative data.
****
# Templates:
### layout.html: 
contains an origin html template which is applied to all site's pages. It has Bootstrap's navbar which is different (thanks to Jinja) for loggined users and not, and also alert messages if flashed is needed.
### register.html:
contains form to register new user. Password is requiered to be at least 8 symbols long, contain digits and both upper and lowercase letters.
### login.html:
contains form to log in a user
### changepass.html:
contain a form to change user's password
### index.html:
page with *generate* button and (optionally) genre select menu, which can fulfill the main purpose of the site - generate the random film from data base.
### generated.html:
contains randomly generated one film's info (poster, title, IMDB's rating, custom genre and rating from our users) it's also has *generate again* button, *watched* to rate film and add it to 'watched' list and *whatch later* button to add it to relative list 
### main.html:
contains a table which keeps track of every film our user whatched and wants to watch later.
### add.html:
a form to add some new film to data base. it's available only when user watched at least 10 filmes
### chat.html:
a live chat where all users can discuss something
### congrats.html:
renders if user watched every films from data base

# CSS and Responsive design:
We used a lot of Bootstrap's elements in order to make our site look beautiful and responsive. But to make it perfectly fit on mobile devices we decided to add on several pages JavaScrpit code to change element's size and/or position according to user's screen resolution.
