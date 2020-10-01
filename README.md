# <img height="45" src="./public/static/icons/128.png" align="top"> Subtitles

Download subtitles for movies, tv shows and anime in your preferred language.

<a href="https://github.com/Spimy/Subtitles/graphs/contributors" alt="Contributors">
  <img src="https://img.shields.io/github/contributors/Spimy/Subtitles"/>
</a>

## Local setup

### Prerequisites

Your system should have these installed before you continue with the local setup:

- Python3 (3.8.x preferably)
- NodeJS

### Installation

1. Install pipenv: `pip install pipenv`.
2. Install python dependencies by running `pipenv install`, which also creates a virtual env.
3. Install node dependencies by running `yarn`.
4. Create the `.env` file and fill it in using the variables listed below.
5. Run `python manage.py migrate` if there are changes made to the database.

#### Environment Variables

Keep the the `SETTING` variable as it is.

```
OPENSUBS_USERNAME=
OPENSUBS_PASSWORD=
SECRET_KEY=
SETTING=subtitles.settings.dev
```

### Running

You can either run the production preview which hosted by Django or run the development server made by Vue with features such as hot reloading which is ideal when developing.

#### Production preview
1. Build the frontend with `yarn build`.
2. Run `pipenv shell` to activate the virtual env environment.
3. Run `python manage.py runserver` to start the server.

#### Development server

You'd need to run two shell instances here, one for the Vue frontend and one for he Django backend which provides the API endpoints.

1. Run `pipenv shell` to activate the virtual environment.
2. Run `python manage.py runserver` to start the Django backend.
3. Run `yarn serve` to start the Vue frontend.
