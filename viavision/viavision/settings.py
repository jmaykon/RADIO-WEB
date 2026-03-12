import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURIDAD ---
# En Render, añade una Variable de Entorno llamada SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-_awsx-00w604l&2qfgh+x6(-53)d^wa6=1=fr#y&a*gj!moi%@')

# DEBUG será False en Render y True en tu PC local
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['via-vision.onrender.com', 'localhost', '127.0.0.1', '.onrender.com']

# --- APLICACIONES ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viewradio', # Tu app principal
]

# --- MIDDLEWARE ---
# WhiteNoise debe ir justo después de SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'viavision.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'viavision.wsgi.application'

# --- BASE DE DATOS ---
# Usa SQLite en local y detecta automáticamente si hay una DB en Render
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- VALIDACIÓN DE CONTRASEÑAS ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- INTERNACIONALIZACIÓN ---
LANGUAGE_CODE = 'es-es' # Cambiado a español
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- ARCHIVOS ESTÁTICOS (CSS, JavaScript, Images) ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Carpeta donde guardas tus archivos estáticos en desarrollo
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Almacenamiento optimizado para producción (comprime archivos)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- CONFIGURACIÓN DE SEGURIDAD PARA PRODUCCIÓN ---
CSRF_TRUSTED_ORIGINS = ['https://via-vision.onrender.com']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'