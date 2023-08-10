# Furniture ecommerce website

 - [Tutorial](https://www.youtube.com/watch?v=jUsm_LV4_cE&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=8), [Tutorial 2](https://www.youtube.com/watch?v=EbLEyM9SyZQ&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh), [tutorial 3](https://www.youtube.com/watch?v=tujhGdn1EMI), [Tutorial 4](https://www.youtube.com/watch?v=xjMP0hspNLE&list=PL-51WBLyFTg1gPEHotYAhNAPsisChkyTc), [tutorial 5](https://www.youtube.com/watch?v=lo7lBD9ynVc&t=14s)

### Instructions
 - Preload pages
 - Add **load more** button
 - Page transition and Animation
 - Fix image size in single product page
 - Show total Cart items on the menu
 - Use Supabase for database solution
 - Use cloudinary for image storage solution
 - The REAL Cost Of AWS, https://planetscale.com/pricing , https://clerk.com/?utm_source=www.google.com&utm_medium=referral&utm_campaign=none
 - SEO For Every single page
 - Create a table with all single data staff of the website such as logo, title, background image, offer, description, and more
 - Make a loader in frontend to fetch data
 - ✅✅ On delete product or category, images should be deleted from the folder too
 - ✅✅ customize django rest framework user password validation
 - ✅✅ Add first name, last name for user
 - Refresh token is not rotating properly
 - ✅✅ Use forget password for user
 - ✅✅ Search by product and category
 - ✅✅ Filter products by different value
 - Use jwt auth token with refresh token
 - Login user with **gmail or username** and **password**
 - ✅✅ One admin panel for admin and staff
 - One customer dashboard
 - Save tokens in client side cookies

### SSLCommerz
 - [Create sandbox account for testing and for production create real account](https://developer.sslcommerz.com/doc/v4/)
 - [Library for python](https://github.com/sslcommerz/SSLCommerz-Python), [API Using curl](https://developer.sslcommerz.com/doc/v4/#initiate-payment)

### BKash API
 - BKash overview - https://www.youtube.com/watch?v=i8TT8-DAF5Q
 - Code - https://www.youtube.com/watch?v=B4xM7rBk2R8&list=PLD11cPzGpfKT1o2OTydIecmyHII5tZl_F&index=2
 - Need a merchant account
 - Request a new product
 - Tokenized checkout overflow - https://developer.bka.sh/docs/tokenized-checkout-overview
 - Token Management Overview - https://developer.bka.sh/docs/token-management-overview-3
 

### Ask about
 - SSLCommerz and product delivery change

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
 - Design -> https://99grid.com/ , https://demo.minimog.co/ , 
 - ecommerce_api - https://github.com/thomas545/ecommerce_api
 - django-ecommerce-api - https://github.com/earthcomfy/django-ecommerce-api/tree/master
 - store-engine - https://github.com/open-ecommerce-api/store-engine/tree/develop
 - The original headless storefront theme for Swell (Nuxt/Vue) - https://github.com/swellstores/origin-theme/tree/master
 - Nuxt 3 and Vue 3 headless eCommerce site with WooCommerce backend and Algolia search - https://github.com/w3bdesign/nuxtjs-woocommerce/tree/master
 - The project utilizes Nuxt3 to create a scalable, efficient, and modern web application. - https://github.com/TutorFx/nuxt3-ecommerce

 - Left at __https://www.youtube.com/watch?v=ktuOUaOyMmo&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=31__

### Reference
 - serializing Objects - > https://www.django-rest-framework.org/api-guide/serializers/#serializing-objects
 - Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.
 - The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
 - Field-level validation -> https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
 - [Overriding predefined model methods](https://docs.djangoproject.com/en/4.2/topics/db/models/#overriding-predefined-model-methods)
 - [Cloudinary's Python SDK provides simple, yet comprehensive image and video upload](https://cloudinary.com/documentation/django_integration)
 - [If you are using Django, you can integrate Cloudinary's uploading capabilities into your forms and models using Cloudinary's helper classes.](https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models)
 - Object-level validation -> https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
 - The following example demonstrates how you might handle creating a user with a nested profile object.
 - .create() and .update() - Override either or both of these to support saving instances.
 - Although Python provides a mail sending interface via the smtplib module, Django provides a couple of light wrappers over it. https://docs.djangoproject.com/en/4.2/topics/email/
 - @classmethod Transform a method into a class method. -> https://docs.python.org/3/library/functions.html?highlight=property#classmethod
 - [decorators in the standard library](https://wiki.python.org/moin/Decorators)
 - [Complete Authentication](https://github.com/celiao/django-rest-authemail)
 - [customize the claims contained in web tokens which are generated by the TokenObtainPairView and TokenObtainSlidingView views, create a subclass for the desired view as well as a subclass for its corresponding serializer. ](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html)
 - 