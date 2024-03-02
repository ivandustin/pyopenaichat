from random import choice
import logging
from openai import ChatCompletion

logger = logging.getLogger(__name__)


def chat(messages, **kwargs):
    default = {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
    }
    kwargs = default | kwargs
    logger.info(f"Parameters\n{kwargs}")
    logger.info(f"Messages\n{messages}")
    response = ChatCompletion.create(messages=messages, **kwargs)
    logger.info(f"Response\n{response}")
    message = choice(response["choices"])["message"]
    return message
