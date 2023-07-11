 - [Tutorial](https://www.youtube.com/watch?v=jUsm_LV4_cE&list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq&index=8)

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