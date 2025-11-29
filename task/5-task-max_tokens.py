from os import getenv
from random import randint
from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

TOKENS_MIN = 10
TOKENS_MAX = 1000

deployment_name = getenv('DIAL_DEPLOYMENT_NAME', 'gpt-4o')
max_tokens = int(getenv('DIAL_MAX_TOKENS', randint(TOKENS_MIN, TOKENS_MAX)))

run(
    deployment_name=deployment_name,
    max_tokens=max_tokens,
    # TODO:
    #  Use `max_tokens` parameter with value 10
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.
