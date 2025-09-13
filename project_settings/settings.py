# """
# Django settings for project_settings project.
# """

# import os

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
# PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '@)0qp0!&-vht7k0wyuihr+nk-b8zrvb5j^1d@vl84cd1%)f=dz'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# # Change and set this to correct IP/Domain
# ALLOWED_HOSTS = ["*"]


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'ml_app.apps.MlAppConfig',
#     'corsheaders'
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware'
# ]

# ROOT_URLCONF = 'project_settings.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.messages.context_processors.messages',
#                 'django.template.context_processors.media'
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'project_settings.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(PROJECT_DIR, 'db.sqlite3'),
#     }
# }


# # Internationalization
# # https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = False

# USE_L10N = False

# USE_TZ = False


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.0/howto/static-files/

# #used in production to serve static files
# STATIC_ROOT = "/home/app/staticfiles/"

# #url for static files
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(PROJECT_DIR, 'uploaded_images'),
#     os.path.join(PROJECT_DIR, 'static'),
#     os.path.join(PROJECT_DIR, 'models'),
# ]

# CONTENT_TYPES = ['video']
# MAX_UPLOAD_SIZE = "104857600"

# MEDIA_URL = "/media/"

# MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploaded_videos')

# #for extra logging in production environment
# if DEBUG == False:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console': {
#                 'class': 'logging.StreamHandler',
#             },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'log.django',
#         },
#         },
#         'loggers': {
#             'django': {
#                 'handlers': ['console','file'],
#                 'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#             },
#         },
#     }

# CORS_ALLOW_ALL_ORIGINS = True
# """
# Django settings for project_settings project.
# """

# import os

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
# PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '@)0qp0!&-vht7k0wyuihr+nk-b8zrvb5j^1d@vl84cd1%)f=dz'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# # Change and set this to correct IP/Domain
# ALLOWED_HOSTS = ["*"]


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'ml_app.apps.MlAppConfig',
#     'corsheaders'
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware'
# ]

# ROOT_URLCONF = 'project_settings.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'django.template.context_processors.media'
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'project_settings.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(PROJECT_DIR, 'db.sqlite3'),
#     }
# }


# # Internationalization
# # https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = False

# USE_L10N = False

# USE_TZ = False


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.0/howto/static-files/

# # URL for static files
# STATIC_URL = '/static/'

# # Directory where static files are collected in production
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')

# # Additional locations of static files
# STATICFILES_DIRS = [
#     os.path.join(PROJECT_DIR, 'static'),
#     os.path.join(PROJECT_DIR, 'uploaded_images'),  # This is where your processed images are stored
# ]

# # Media files (uploaded videos)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploaded_videos')

# CONTENT_TYPES = ['video']
# MAX_UPLOAD_SIZE = 104857600  # 100MB in bytes (changed from string to integer)

# # Create necessary directories if they don't exist
# os.makedirs(MEDIA_ROOT, exist_ok=True)
# os.makedirs(os.path.join(PROJECT_DIR, 'uploaded_images'), exist_ok=True)
# os.makedirs(os.path.join(PROJECT_DIR, 'static'), exist_ok=True)

# #for extra logging in production environment
# if DEBUG == False:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console': {
#                 'class': 'logging.StreamHandler',
#             },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'log.django',
#         },
#         },
#         'loggers': {
#             'django': {
#                 'handlers': ['console','file'],
#                 'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#             },
#         },
#     }

# CORS_ALLOW_ALL_ORIGINS = True

# """
# Django settings for project_settings project.
# """

# import os

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
# PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY', '@)0qp0!&-vht7k0wyuihr+nk-b8zrvb5j^1d@vl84cd1%)f=dz')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# # Detect if we're running on Render
# # Detect if we're running on Render - use a different approach
# RENDER = os.environ.get('RENDER', '').lower() == 'true'

# # Change and set this to correct IP/Domain
# if RENDER:
#     # Production settings
#     ALLOWED_HOSTS = [
#         'https://deepguard-backend-ny4m.onrender.com',  # ← CHANGE THIS to your actual Render URL
#         'https://deep-guard-frontend.vercel.app/',   # ← CHANGE THIS to your actual Vercel URL
#         'localhost',
#         '127.0.0.1'
#     ]
# else:
#     # Development settings
#     ALLOWED_HOSTS = ["*"]

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'ml_app.apps.MlAppConfig',
#     'corsheaders'
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # Add whitenoise
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware'
# ]

# ROOT_URLCONF = 'project_settings.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.messages.context_processors.messages',
#                 'django.template.context_processors.media'
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'project_settings.wsgi.application'

# # Database - Since you're not using a database, we'll use a minimal configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',  # Use dummy backend since no database is needed
#     }
# }

# # Internationalization
# # https://docs.djangoproject.com/en/3.0/topics/i18n/
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = False
# USE_L10N = False
# USE_TZ = False

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.0/howto/static-files/
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')

# # Additional locations of static files
# STATICFILES_DIRS = [
#     os.path.join(PROJECT_DIR, 'static'),
# ]

# # Media files (uploaded videos)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploaded_videos')

# CONTENT_TYPES = ['video']
# MAX_UPLOAD_SIZE = 104857600  # 100MB in bytes

# # Create necessary directories if they don't exist
# os.makedirs(MEDIA_ROOT, exist_ok=True)
# os.makedirs(os.path.join(PROJECT_DIR, 'uploaded_images'), exist_ok=True)
# os.makedirs(os.path.join(PROJECT_DIR, 'static'), exist_ok=True)
# os.makedirs(STATIC_ROOT, exist_ok=True)

# # CORS settings
# if RENDER:
#     CORS_ALLOWED_ORIGINS = [
#         "https://deep-guard-frontend.vercel.app/",  # ← CHANGE THIS to your Vercel URL
#         "http://localhost:3000",
#         "http://127.0.0.1:3000",
#     ]
#     CSRF_TRUSTED_ORIGINS = [
#         "https://deepguard-backend-ny4m.onrender.com",  # ← CHANGE THIS to your Render URL
#         "https://deep-guard-frontend.vercel.app/",   # ← CHANGE THIS to your Vercel URL
#     ]
# else:
#     CORS_ALLOW_ALL_ORIGINS = True

# # Security settings for production
# if RENDER:
#     # Security settings
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
#     SECURE_BROWSER_XSS_FILTER = True
    
#     # Whitenoise configuration
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# # Logging configuration
# if not DEBUG:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console': {
#                 'class': 'logging.StreamHandler',
#             },
#             'file': {
#                 'level': 'DEBUG',
#                 'class': 'logging.FileHandler',
#                 'filename': 'log.django',
#             },
#         },
#         'loggers': {
#             'django': {
#                 'handlers': ['console','file'],
#                 'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             },
#         },
#     }

# # For serving uploaded_images in production
# if RENDER:
#     STATICFILES_DIRS.append(('uploaded_images', os.path.join(PROJECT_DIR, 'uploaded_images')))


import os
# Add to your settings.py
import torch
torch.set_num_threads(1)  # Limit PyTorch to 1 thread

# Reduce OpenCV memory usage

os.environ['OPENCV_IO_MAX_IMAGE_PIXELS'] = '1000000000'  # 1GB limit

# Build paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', '@)0qp0!&-vht7k0wyuihr+nk-b8zrvb5j^1d@vl84cd1%)f=dz')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
RENDER = os.environ.get('RENDER', '').lower() == 'true'

# ALLOWED_HOSTS - FIXED
ALLOWED_HOSTS = [
    'deepguard-backend-ny4m.onrender.com',  # ✅ Correct format
    'localhost',
    '127.0.0.1',
    '*'
]

# Applications
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ml_app.apps.MlAppConfig',
    'corsheaders'
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

# URLs and Templates
ROOT_URLCONF = 'project_settings.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'project_settings.wsgi.application'

# Database - FIXED
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

# Static Files - FIXED
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(PROJECT_DIR, 'uploaded_images'),  # ✅ Added this
]

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploaded_videos')
CONTENT_TYPES = ['video']
MAX_UPLOAD_SIZE = 104857600

# Create directories
os.makedirs(MEDIA_ROOT, exist_ok=True)
os.makedirs(os.path.join(PROJECT_DIR, 'uploaded_images'), exist_ok=True)
os.makedirs(os.path.join(PROJECT_DIR, 'static'), exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

# CORS - FIXED
CORS_ALLOW_ALL_ORIGINS = True  # ✅ Simplified for now

# Security for production
if RENDER:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Logging
if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {'class': 'logging.StreamHandler'},
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'log.django',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console','file'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            },
        },
    }