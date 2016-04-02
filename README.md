# Portfolio
My Python / Django Portfolio

### Instructions:
Let's first install what we need (in case you didn't already)
```
pip install Django
pip install MySQL-python
```

##### Install Django Summernote
Django Summernote is the text editor being used to generate styled texts inside Django's Admin area. Install it running:
```
pip install django-summernote 
```

##### Create your local_settings.py in the root folder, in which should contain something like this (or any extra settings that you need):

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '[your secret key here]'
DEBUG = True

# Check settings.py for more information on how to set this
DATABASES = {[__your_database_settings__]}

# Copy the TEMPLATES declaration from settings.py and change what you need. 'DIRS', for example.
TEMPLATES = [{	        
	'DIRS': [os.path.dirname(BASE_DIR) + '',],
},]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_DIRS = [os.path.dirname(BASE_DIR) + '/templates/',]
STATIC_ROOT = os.path.dirname(BASE_DIR) + '/'
STATIC_URL = '/static/'
```