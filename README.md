# Furniture ecommerce website

 - [Tutorial](https://www.youtube.com/watch?v=jUsm_LV4_cE&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=8), [Tutorial 2](https://www.youtube.com/watch?v=EbLEyM9SyZQ&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh), [tutorial 3](https://www.youtube.com/watch?v=tujhGdn1EMI)

 - Setup
 ```
 mkdir furniture-ecom
 cd furniture-ecom/
 python3 -m venv virtual-env
 source virtual-env/bin/activate
 clear
 pip install Django==4.2.3
 django-admin startproject drfecom
 cd drfecom/
 ./manage.py runserver
 ```
 - Secret key with shell
 ```
 python3 manage.py shell
 >>> from django.core.management.utils import get_random_secret_key
 >>> print(get_random_secret_key())
 ```
 - Testing the project
 ```
 pip install pytest
 pytest --help
 pip install pytest-django
 pytest
 ```
 - Use `black` for formatting code
 - Use `flake8` for linting the code
 - Create super user `./manage.py createsuperuser`
 - Create schema for api documentation `./manage.py spectacular --file schema.yml`
 - Running tests with coverage
 ```
 coverage
 coverage html
 coverage run -m pytest
 pytest --cov
 ```

### Inspirations
 - django-rest-framework-json-api - https://github.com/django-json-api/django-rest-framework-json-api
 - Django REST Registration - https://github.com/apragacz/django-rest-registration
 - deep-dive-drf-model-serializer-relations - https://github.com/oscarychen/deep-dive-drf-model-serializer-relations
 - ecommerce_api - https://github.com/thomas545/ecommerce_api

 - Left at __https://www.youtube.com/watch?v=ktuOUaOyMmo&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=31__