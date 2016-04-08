# Portfolio
My Python / Django Portfolio

### Instructions:
Let's first install what we need

##### Installing the dependencies
Run the following commands to install the dependencies:
```
pip install Django
pip install MySQL-python
pip install django-summernote 
pip install django-autocomplete-light
pip install Pillow
```

##### Create your local_settings.py in the root folder, in which should contain something like this (or any extra settings that you need):

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '[your secret key here]'
DEBUG = True

# Check settings.py for more information on how to set this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
    },
}

# Copy the TEMPLATES declaration from settings.py and change what you need. 'DIRS', for example.
TEMPLATES = [{	        
	'DIRS': [os.path.dirname(BASE_DIR) + '',],
},]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_DIRS = (
    os.path.dirname(BASE_DIR) + '/templates/',
)

STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
MEDIA_ROOT  = os.path.join(BASE_DIR, '/media')

STATIC_URL  = '/static/'
MEDIA_URL   = '/media/'
```