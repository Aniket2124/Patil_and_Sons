from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomAuthn(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            print('Authentication Successful')
            # return user if user.check_password(password) else None

            if user.check_password(password) and user.is_superuser:
                user.is_active = True
                user.save()
                return user 
            else:
                return None

        except User.DoesNotExist:
            return None


