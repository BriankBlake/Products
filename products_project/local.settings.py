# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a-eh#i4p+yz+_kdr@y9na6g)x_$j_g(v6tuzx65pb(ly8pec!b'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'hatemenow',
    }
}