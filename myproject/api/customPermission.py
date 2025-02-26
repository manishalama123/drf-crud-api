from rest_framework.permissions import BasePermission
#Custom Permission
class UserDetails(BasePermission):
    def has_object_permission(self,request, obj, view):
        if request.method in ['GET','HEAD','OPTIONS']:
            return True

        if request.method in ['PUT','PATCH'] and obj == request.user:
            return True
        
        if request.method in ['DELETE'] and request.user.is_staff:
            return True
        
        return False