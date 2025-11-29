from os import getenv
from random import randint
from task.app.main import run

# TODO:
#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User massage: Name a random animal

SEED_MIN = 1
SEED_MAX = 1000

deployment_name = getenv('DIAL_DEPLOYMENT_NAME', 'gpt-4o')
seed = int(getenv('DIAL_SEED', randint(SEED_MIN, SEED_MAX)))

run(
    deployment_name=deployment_name,
    seed=seed,
    # TODO:
    #  1. Use `seed` parameter with value 42 (or whatever you want)
    #  2. Use `n` parameter with value 5
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.
# For Anthropic and Gemini this parameter will be ignored
