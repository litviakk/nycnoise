### onboarding

- clone the repo
- check that you have Python 3.10 or 3.11 locally installed and working
- check that you have Postgres locally up and running
  - recommended on Macs: use/install [Postgres.app](https://postgresapp.com/) which is a full featured database-in-an-app
  - also recommended on Macs: [Postico](https://eggerapps.at/postico2/) which is a local database GUI
- create a local database
  - recommended on Macs: start Postgres.app, open Postico, connect to localhost with all of the defaults (your computer's username, no password, localhost, port 5432), create a database named `nycnoise`
- duplicate `.env.example` to `.env` and fill out the values
- create a python virtual environment to store/manage the project's dependencies locally:
  - create the virtual environment: `python3 -m venv venv`
  - activate it: `source venv/bin/activate`
  - your terminal should now have a `(venv)` prefix -- this means you're in the virtual environment
- install the dependencies with the venv activated: `pip install -r requirements.txt`
- (almost there!)
- run the migrations: `python manage.py migrate`
  - if this works, that means that Django can talk to your local database. that's really great!
  - if you have trouble here - it could be due to the Postgres server not running or the database doesn't exist, or the connection string in `.env` is wrong
- create a superuser: `python manage.py createsuperuser`
  - locally, I recommend `admin`/`admin` (username/password) and a made up email like `a@a.ca`
  - you will get a warning about the bad password :-) ignore it :-) (it's fine for local development)
- run the server: `python manage.py runserver`
  - you should be able to visit `localhost:8000` and see the site
  - you should be able to visit `localhost:8000/admin` and log in with the superuser you just created
- you're all set!