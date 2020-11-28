from rest_framework import permissions

from accounts.utils import check_user_type
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IsOwnerOrSponsorStaffReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if (request.method in permissions.SAFE_METHODS
                and check_user_type(request.user) in ["sponser", "staff"]):
            return True
        print(request.user)
        try:
            user_obj = obj.student.user
        except AttributeError:
            user_obj = obj.user
        print(user_obj == request.user)
        return user_obj == request.user


class SponseeOrStaffReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        user_type = check_user_type(request.user)
        print(user_type)
        if(user_type == "sponsee"):
            return False
        if request.method in permissions.SAFE_METHODS:
            return True


class MyPermissionMixin:
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated & SponseeOrStaffReadOnly]
        elif (self.action in ['retrieve', 'update', 'partial_update', 'create']):
            print("hrllp")
            permission_classes = [IsAuthenticated &
                                  IsOwnerOrSponsorStaffReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
