import os
import logging
from openai import OpenAI

logger = logging.getLogger('app')

# fetch LLM configurations from .env
LLM_PROVIDER = os.getenv('LLM_PROVIDER')
LLM_ENDPOINT = os.getenv('LLM_ENDPOINT')
LLM_MODEL = os.getenv('LLM_MODEL')
LLM_API_KEY = os.getenv('LLM_API_KEY')

client = OpenAI(
    api_key=LLM_API_KEY,
    base_url=LLM_ENDPOINT
)

DEFAULT_SYSTEM_PROMPT = """\
你是一点星辰公司的法律机器人。
"""

SUMMARY_SYSTEM_PROMPT = """\
你是一点星辰公司的法律机器人。当前的对话内容。
"""

PRIORITY_SYSTEM_PROMPT = """\
你是一点星辰公司的法律机器人。当前的对话内容。
"""


def generate_chat_completion(messages):
    """This function generates a chat completion based on the messages provided.

    Args:
        messages (list): the list of messages in the chat

    Returns:
        dict: message and reservation_intent.
    """

    # inject system prompt
    messages.insert(0, {
        "role": "system",
        "content": DEFAULT_SYSTEM_PROMPT
    })

    # TODO: implement error handling for LLM API
    # completion = client.create_chat_completion(
    #     model=LLM_MODEL,
    #     messages=messages
    # )
    completion = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages
    )

    choice = completion.choices[0]

    # TODO: implement logic to determine reservation_intent
    reservation_intent = "false"

    logger.debug(f"Chat completion: {choice.message.content}")
    return {
        "message": choice.message.content,
        "reservation_intent": reservation_intent
    }


def generate_chat_summary(messages):
    """This function generates a chat summary based on the messages provided.

    Args:
        messages (list): the list of messages in the chat

    Returns:
        dict: message and reservation_intent.
    """

    # inject system prompt
    messages.insert(0, {
        "role": "system",
        "content": SUMMARY_SYSTEM_PROMPT
    })

    completion = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages
    )

    choice = completion.choices[0]

    logger.debug(f"Chat summary: {choice.message.content}")
    return {
        "summary": choice.message.content
    }


def determine_chat_priority(messages):
    """This function determines the priority of the chat based on the messages provided.

    Args:
        messages (list): the list of messages in the chat

    Returns:
        dict: priority.
    """

    # inject system prompt
    messages.insert(0, {
        "role": "system",
        "content": PRIORITY_SYSTEM_PROMPT
    })

    completion = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages
    )

    choice = completion.choices[0]

    logger.debug(f"Chat priority: {choice.message.content}")

    return {
        "priority": choice.message.content
    }
