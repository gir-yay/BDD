
#pour manager 
from django.contrib.auth.decorators import user_passes_test

def is_manager(user):
    return user.is_authenticated and user.type == 'manager'
#===============================================================
#===============================================================