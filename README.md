# Portfolio
My Python / Django Portfolio

### Instructions:
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