from accounts.models import User


def check_user_type(user_obj):
    if(user_obj.is_staff):
        return "staff"
    try:
        the_user = user_obj.sponsee
        return "sponsee"
    except User.sponsee.RelatedObjectDoesNotExist:
        the_user = None

    try:
        the_user = user_obj.sponser
        return "sponser"
    except User.sponser.RelatedObjectDoesNotExist:
        return None
