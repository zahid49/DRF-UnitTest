from rest_framework.permissions import BasePermission


class UserIsOwnerTodo(BasePermission):

    def has_object_permission(self, request, view, todo):
        return request.user.id == todo.user.id
