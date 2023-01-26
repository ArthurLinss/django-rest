# Django Rest

Example project for the usage of django rest framework within django web framework. Also relies on django-environ.

# Setup

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install django-environ

# Information

Django Rest: https://www.django-rest-framework.org/
Tutorial: https://www.django-rest-framework.org/tutorial/1-serialization/

The following packages are optional:

- PyYAML, uritemplate (5.1+, 3.0.0+) - Schema generation support. (pip install PyYAML)
- Markdown (3.0.0+) - Markdown support for the browsable API. (pip install Markdown)
- Pygments (2.4.0+) - Add syntax highlighting to Markdown processing.
- django-filter (1.0.1+) - Filtering support.
- django-guardian (1.1.1+) - Object level permissions support.

# Django

- General: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
- python manage.py createsuperuser --email admin@example.com --username admin
- python manage.py migrate
- python manage.py makemigrations
- python manage.py runserver
- check in browser: http://127.0.0.1:8000/

# Virtual Environment
- python3 -m venv venv
- source venv/bin/activate
- (deactivate)

# Django Environ
- https://django-environ.readthedocs.io/en/latest/quickstart.html

# External Script
- To use django models in an external script (instead of python manage.py shell), you need the following at the beginning of your script
`
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django

django.setup()
`
