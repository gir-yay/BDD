"""

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Manager
class ManagerAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            manager = Manager.objects.get(username=username)
            if check_password(password, manager.password):
                return manager
        except Manager.DoesNotExist:
            pass
        return None
    """