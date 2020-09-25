# Subtitles

Download subtitles for movies, tv shows and anime in your preferred language.

## Running locally

### Prerequisites

Your system should have these installed before you continue with the local setup:

- Python3 (3.8.x preferably)
- NodeJS

### Installation

1. Install pipenv: `pip install pipenv`.
2. Install python dependancies by running `pipenv install`, which also creates a virtual env.
3. Install node dependancies by running `yarn`.
4. Create the `.env` file and fill it in using the variables listed under [environment variables section](#environment-variables).
5. Run `pipenv shell` to activate the virtual env and load `.env` variables.
6. Run `python manage.py runserver` to start the development server. _(local-only)_

## Environment Variables

Keep the the `SETTING` variable as it is.

```
SECRET_KEY=secret_key
SETTING=subtitles.settings.dev
```
