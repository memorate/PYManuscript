from pprint import *


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics',
                             age=18,
                             married=False)
pprint(user_profile)
