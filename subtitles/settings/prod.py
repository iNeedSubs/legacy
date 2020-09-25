from .base import *


DEBUG = False


INSTALLED_APPS += [
    'cloudinary_storage',
    'cloudinary'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME'),
        'HOST': os.getenv('DATABASE_HOST'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASS'),
        'PORT': 5432,
    }
}


MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUD_KEY'),
    'API_SECRET': os.getenv('CLOUD_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/subtitles/media/'
MEDIA_ROOT = BASE_DIR / 'subtitles' / 'media'

CORS_ORIGIN_ALLOW_ALL = False
