from rest_framework import permissions
from .permissions import IsStaffEditorPermission, IsGeneralUserPermission

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

class GeneralUserPermissionMixin():
    permission_classes = [permissions.IsAuthenticated, IsGeneralUserPermission]