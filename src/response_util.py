from flask import jsonify


class HTTPStatusCode:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503


class HTTPStatusMessage:
    OK = "OK"
    CREATED = "Resource created successfully"
    ACCEPTED = "Request accepted"
    NO_CONTENT = "No content"
    BAD_REQUEST = "Bad request"
    UNAUTHORIZED = "Unauthorized access"
    FORBIDDEN = "Forbidden access"
    NOT_FOUND = "Resource not found"
    METHOD_NOT_ALLOWED = "Method not allowed"
    CONFLICT = "Conflict occurred"
    INTERNAL_SERVER_ERROR = "Internal server error"
    SERVICE_UNAVAILABLE = "Service unavailable"


def make_response(http_status_code, http_status_message, data=None):
    default_response = {
        "result_message": http_status_message
    }

    # merge the default response with the data, if it exists
    if data:
        default_response.update(data)

    return jsonify(default_response), http_status_code
