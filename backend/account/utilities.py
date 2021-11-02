import datetime

import jwt
from django.conf import settings

def generate_access_token(uuid):

    payload = {
        "uuid": str(uuid),
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=30),
        "iat": datetime.datetime.now(),
    }

    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return access_token

def generate_refresh_token(uuid):

    payload = {
        "uuid": str(uuid),
        "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
        "iat": datetime.datetime.now(),
    }

    refresh_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return refresh_token