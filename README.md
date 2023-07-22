# Furniture ecommerce website

 - [Tutorial](https://www.youtube.com/watch?v=jUsm_LV4_cE&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=8), [Tutorial 2](https://www.youtube.com/watch?v=EbLEyM9SyZQ&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh), [tutorial 3](https://www.youtube.com/watch?v=tujhGdn1EMI), [Tutorial 4](https://www.youtube.com/watch?v=xjMP0hspNLE&list=PL-51WBLyFTg1gPEHotYAhNAPsisChkyTc), [tutorial 5](https://www.youtube.com/watch?v=lo7lBD9ynVc&t=14s)

### Instructions
 - On delete product or category, images should be deleted from the folder too
 - Search by product and category
 - Filter products by different value
 - For frontend user gatsby js, and typescript, and materaize css
 - Gatsby tutorial - https://www.youtube.com/watch?v=e7sqKE0ODdI
 - Use jwt auth token with refresh token
 - Login user with **gmail or username** and **password**
 - One admin panel for admin and staff
 - One customer dashboard
 - Save tokens in client side cookies

### Deployment
 - Docarize the application
 - Setup postgres database
 - Change environment variables
 - Create superuser in django
 - Remove default django admin 


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
 - ecommerce_api - https://github.com/thomas545/ecommerce_api
 - django-ecommerce-api - https://github.com/earthcomfy/django-ecommerce-api/tree/master
 - store-engine - https://github.com/open-ecommerce-api/store-engine/tree/develop

 - Left at __https://www.youtube.com/watch?v=ktuOUaOyMmo&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=31__

### Reference
 - serializing Objects - > https://www.django-rest-framework.org/api-guide/serializers/#serializing-objects
 - Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.
 - The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
 - Field-level validation -> https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
 - Object-level validation -> https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
 - The following example demonstrates how you might handle creating a user with a nested profile object.
 - .create() and .update() - Override either or both of these to support saving instances.
 - Although Python provides a mail sending interface via the smtplib module, Django provides a couple of light wrappers over it. https://docs.djangoproject.com/en/4.2/topics/email/
 - @classmethod Transform a method into a class method. -> https://docs.python.org/3/library/functions.html?highlight=property#classmethod
 - decorators in the standard library, -> https://wiki.python.org/moin/Decorators
