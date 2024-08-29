from functools import wraps
from flask import request, jsonify
from src.response_util import make_response, HTTPStatusCode, HTTPStatusMessage
import logging
import os

logger = logging.getLogger('app')

CLIENT_API_KEY = os.getenv('CLIENT_API_KEY')
# assert client api key is set and not empty
assert CLIENT_API_KEY, "CLIENT_API_KEY not set in .env file."


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('Authorization')
        if api_key and api_key.startswith("Bearer "):
            api_key = api_key.split(" ")[1]
            if api_key == CLIENT_API_KEY:
                return f(*args, **kwargs)

        # default response for unauthorized access
        logger.warning("Unauthorized access attempt.")
        return make_response(HTTPStatusCode.UNAUTHORIZED, HTTPStatusMessage.UNAUTHORIZED)

    return decorated_function
