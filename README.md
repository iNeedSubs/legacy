# Subtitles

Download subtitles for movies, tv shows and anime in your preferred language.


## Contributions

1. Make sure you have python 3 installed. Preferably 3.8.x
2. Make sure you have nodejs installed
3. Install pipenv: `pip install pipenv`
4. Install all requirements using `pipenv install` which should also create a virtual env
5. Install all requirements using `yarn`
6. Create a `.env` file with the variables in [environment variables section](#environment-variables)
7. Run `pipenv shell` to activate the virtual env and load `.env` vars
8. Run `python manage.py runserver` to start the development server

NEVER run 8 for production. Gunicorn should deal with start the server for production set inside
of Procfile.


## Environment Variables

Database and cloudinary related variables are only needed for production.
No need for them if you are developing on a local machine.

SETTING var is either `subtitles.settings.dev` or `subtitles.settings.prod`.
Use dev on local machine and prod on host.

HOST is the URL of the web app. Leave this blank local machine.

```
SECRET_KEY=secret_key
DATABASE_NAME=database_name
DATABASE_HOST=database_host
DATABASE_USER=database_username
DATABASE_PASS=database_password
CLOUD_NAME=cloudinary_name
CLOUD_KEY=cloudinary_key
CLOUD_SECRET=cloudinary_secret
SETTING=setting
HOST=host
```
