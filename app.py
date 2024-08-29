from flask import Flask, jsonify, request, abort

import app_global
from src.auth_util import require_api_key
from src.response_util import make_response, HTTPStatusCode, HTTPStatusMessage
from src.services.chat_service import generate_chat_completion, generate_chat_summary, determine_chat_priority
from dotenv import load_dotenv
import os

app = Flask(__name__)


@app.before_request  # all the routes in this app require an API key
@require_api_key
def before_request():
    pass


@app.route('/')
def smoke():
    return make_response(HTTPStatusCode.OK, HTTPStatusMessage.OK)


@app.route('/v1/chat/completions', methods=['POST'])
@require_api_key
def chat_completions():
    data = request.get_json()
    '''
    input data validation
    1. messages should be a non-empty list
    2. each message should be a dictionary with role and content keys
    3. role should be either 'user' or 'assistant'
    '''
    if 'messages' not in data or not data['messages']:
        return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

    for message in data['messages']:
        if not isinstance(message, dict) or 'role' not in message or 'content' not in message:
            return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

        if message['role'] not in ['user', 'assistant']:
            return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

    response = generate_chat_completion(data['messages'])

    return make_response(HTTPStatusCode.OK, HTTPStatusMessage.OK, response)


@app.route('/v1/chat/summary', methods=['POST'])
@require_api_key
def chat_summary():
    data = request.get_json()
    '''
    input data validation
    1. messages should be a non-empty list
    2. each message should be a dictionary with role and content keys
    3. role should be either 'user' or 'assistant'
    '''
    if 'messages' not in data or not data['messages']:
        return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

    for message in data['messages']:
        if not isinstance(message, dict) or 'role' not in message or 'content' not in message:
            return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

        if message['role'] not in ['user', 'assistant']:
            return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

    response = generate_chat_summary(data['messages'])

    return make_response(HTTPStatusCode.OK, HTTPStatusMessage.OK, response)


@app.route('/v1/chat/priority', methods=['POST'])
@require_api_key
def chat_priority():
    data = request.get_json()
    '''
    input data validation
    1. messages should be a non-empty list
    2. each message should be a dictionary with role and content keys
    3. role should be either 'user' or 'assistant'
    '''
    if 'messages' not in data or not data['messages']:
        return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

    for message in data['messages']:
        if not isinstance(message, dict) or 'role' not in message or 'content' not in message:
            return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

        if message['role'] not in ['user', 'assistant']:
            return make_response(HTTPStatusCode.BAD_REQUEST, HTTPStatusMessage.BAD_REQUEST)

    response = determine_chat_priority(data['messages'])

    return make_response(HTTPStatusCode.OK, HTTPStatusMessage.OK, response)


if __name__ == '__main__':
    app.run(debug=True)
