from rest_framework import permissions

"""
This permission class ties into Django's standard django.contrib.auth model permissions. This permission must only be applied to views that have a .queryset property or get_queryset() method. https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions
[To implement a custom permission, override BasePermission and implement either, or both, of the following methods](https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions)
"""

# class IsStaffEditorPermission(permissions.DjangoModelPermissions):
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTIONS': [],
#         'HEAD': [],
#         'POST': ['%(app_label)s.add_%(model_name)s'],
#         'PUT': ['%(app_label)s.change_%(model_name)s'],
#         'PATCH': ['%(app_label)s.change_%(model_name)s'],
#         'DELETE': ['%(app_label)s.delete_%(model_name)s'],
#     }
    # def has_permission(self, request, view):
    #     if not request.user.is_staff():
    #         return False 
    #     return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     print(request.user.get_all_permissions())
    #     print(request.user)
    #     print(request.user.is_staff)
    #     if request.user.is_staff:
    #         if request.user.has_perm("peroducts.view_product"):
    #             return True
    #         if request.user.has_perm("peroducts.change_product"):
    #             return True
    #         if request.user.has_perm("peroducts.add_product"):
    #             return True
    #         if request.user.has_perm("peroducts.delete_product"):
    #             return True
    #     return False 
    
    # def has_object_permission(self, request, view, obj):
    #     print("obj.owner == request.user: ", obj.owner == request.user)
    #     return obj.owner == request.user


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    
class IsGeneralUserPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        # print(request.user.get_all_permissions())
        if request.user.is_active:
            return True
        return False


