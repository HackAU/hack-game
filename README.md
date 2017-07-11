# TheGame

# Setup
Sass is required to build TheGame: `sudo gem install sass`

Python 3 is required. `pip install -r requirements`

#### Settings setup
Edit game/settings.py according to your needs:

- **STATIC_ROOT**: Where your static files will be placed
- **EVENT_START** and **EVENT_DURATION**.
- **TIME_ZONE**.
- **LEVEL_INFO**: Array where i-th entry is a tuple, with the html filename and the solution to the i-th level.
- **ALLOWED_HOSTS** as convenience.

Run sass script: `./sassit.sh`

`python manage.py collectstatic`

`python manage.py migrate`

`python manage.py runserver 0.0.0.0:8000`

# Adding new levels
Right now, levels are located in gameapp/templates/levels/. Put your level in a html, and add a new entry to `LEVEL_INFO`. The i-th entry is the i-th level.

#original requirement: 
psycopg
