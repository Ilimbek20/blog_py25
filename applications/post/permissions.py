from rest_framework.permissions import BasePermission, SAFE_METHODS

# user1, user2
# post/1/ user1
# post2 2 user2

class IsOwner(BasePermission):
    
    def has_permission(self, request, view):
        # print(request.method)
        # print(request.user.is_authenticated)
        # print(SAFE_METHODS)
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated
        

    def has_object_permission(self, request, view, obj): # GET by id, PUT, PATCH, DELETE
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user == obj.owner
