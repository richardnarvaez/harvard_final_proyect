from .models import User

class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):
        print(username,password, "IS THIS WORKING")
        try:
            print(username,password, "IS THIS WORKING")
            user = User.object.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            print("User does not exist")
            return None

    def get_user(self,user_id):
        try:
            user = User.object.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            print("User does not exist")
            return None