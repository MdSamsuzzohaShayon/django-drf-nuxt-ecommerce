# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.authtoken.models import Token # Use simple JWT instead

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError

"""
serializing Objects - > https://www.django-rest-framework.org/api-guide/serializers/#serializing-objects
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.
The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
Field-level validation -> https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
Object-level validation -> https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
The following example demonstrates how you might handle creating a user with a nested profile object.
.create() and .update() - Override either or both of these to support saving instances.
"""
class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True) # need to validate by external validators , validators=[validate_password]
    confirm_password = serializers.CharField(write_only=True)

    # To do any other validation that requires access to multiple fields, add a method called .validate()
    def validate(self, data):
        print("validate", data)
        password = data.get('password')
        confirm_password = data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Password did not match!")
        return data
    
    def create(self, validated_data):
        print("Create -> ", validated_data)
        try:
            user = get_user_model().objects.create_user(**validated_data)
            user.save()
            return user
        except IntegrityError as e:
            raise serializers.ValidationError({'email': ['This email address is already taken.']}) 