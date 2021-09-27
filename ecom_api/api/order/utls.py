#============== helper functions =====================#

from django.contrib.auth import get_user_model


def validated_user_session(id,token):
    """validated the user token_session"""
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False

    except UserModel.DoesNotExist:
        return False