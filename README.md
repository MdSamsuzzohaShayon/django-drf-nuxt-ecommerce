# Furniture ecommerce website

 - [Tutorial](https://www.youtube.com/watch?v=jUsm_LV4_cE&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=8), [Tutorial 2](https://www.youtube.com/watch?v=EbLEyM9SyZQ&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh), [tutorial 3](https://www.youtube.com/watch?v=tujhGdn1EMI), [Tutorial 4](https://www.youtube.com/watch?v=xjMP0hspNLE&list=PL-51WBLyFTg1gPEHotYAhNAPsisChkyTc), [tutorial 5](https://www.youtube.com/watch?v=lo7lBD9ynVc&t=14s)

### Instructions
 - On delete product or category, images should be deleted from the folder too
 - Search by product and category
 - Filter products by different value

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
 - https://99grid.com/
 - django-rest-framework-json-api - https://github.com/django-json-api/django-rest-framework-json-api
 - Django REST Registration - https://github.com/apragacz/django-rest-registration
 - ecommerce_api - https://github.com/thomas545/ecommerce_api

 - Left at __https://www.youtube.com/watch?v=ktuOUaOyMmo&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=31__
