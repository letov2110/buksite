
from pathlib import Path,os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-qt!@_dp)fegad_!jcs#d*_fh5=%&rt)_wv!00r&1qqb&_bef5v'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','178.128.243.102','.buksite.space','buksite.space']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apl',
    'rest_framework',
    'tinymce',
    'reglog',
    'tutor',
    'newart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


INTERNAL_IPS = [
    # ...
    "localhost",
    "127.0.0.1", 
]
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

ROOT_URLCONF = 'chtoto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chtoto.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'yury',
        'PASSWORD': 'yury',
        'HOST': 'localhost',
        'PORT': '',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",BASE_DIR / "media",
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PROJECT_DIR = os.path.dirname(__file__)

TINYMCE_SPELLCHECKER = True
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
# TINYMCE_JS_ROOT = os.path.join(STATICFILES_DIRS, "tinymce")
static_dir = None
for directory in STATICFILES_DIRS:
    if directory:  # Check if directory is not empty
        static_dir = directory
        break  # Exit the loop after finding the first non-empty directory

if static_dir:
    TINYMCE_JS_ROOT = os.path.join(static_dir, "tinymce")
else:
    # Handle the case where no static directories are configured (optional)
    raise ValueError("No static directories found in STATICFILES_DIRS")


FILEBROWSER_DIRECTORY = '/home/yury/'
DIRECTORY = ''

X_FRAME_OPTIONS = 'SAMEORIGIN'

TINYMCE_DEFAULT_CONFIG = {
    "relative_urls": False,
    "remove_script_host": False,
    "convert_urls": True,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',

    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    "language": "en_US",
}
