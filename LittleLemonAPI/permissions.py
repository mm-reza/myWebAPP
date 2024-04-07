from rest_framework import permissions
# from rest_framework.authentication import TokenAuthentication

class IsManager(permissions.BasePermission):
    # authentication_classes = [TokenAuthentication]
    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True

class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='delivery crew').exists():
            return True
