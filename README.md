# Pre-hackathon Hacking Game

# Setup
Sass is required to build css: `sudo gem install sass`

Python 3 is required as well as sepecified dependencies `pip install -r requirements.txt`

#### Settings setup

- **EVENT_START** and **EVENT_DURATION**.
- **TIME_ZONE**.
- **LEVEL_INFO**: Array where i-th entry is a tuple, with the html filename and the solution to the i-th level.
- **ALLOWED_HOSTS** as convenience.

#### Running locally
compile Sass files: `gulp sass`

init DB tables: `python manage.py migrate`

run server: `python manage.py runserver 0.0.0.0:8000`

#### Deploy to Heroku

configure heruko buildpack for post/pre script exec using node package.json:
`heroku buildpacks:set heroku/python -a hack-game`<br>
`heroku buildpacks:add --index 1 heroku/nodejs -a hack-game`<br>

add scripts like that:
`
"scripts": {
    "postinstall": "gulp sass"
  }
`

added Procfile which will migrate db and start server:
`web: python manage.py migrate & python manage.py runserver 0.0.0.0:$PORT
`


# credits
originally forked from HackUPC 
