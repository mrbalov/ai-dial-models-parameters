from os import getenv
from random import uniform
from task.app.main import run

# TODO:
#  Try `presence_penalty` parameter.
#  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's
#  likelihood to talk about new topics. Higher values == more topic diversity.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: What is an entropy in LLM's responses?

PP_MIN = -2.0
PP_MAX = 2.0

deployment_name = getenv('DIAL_DEPLOYMENT_NAME', 'gpt-4o')
presence_penalty = float(getenv('DIAL_PRESENCE_PENALTY', uniform(PP_MIN, PP_MAX)))

run(
    deployment_name=deployment_name,
    print_only_content=True,
    presence_penalty=presence_penalty,
    # TODO:
    #  Use `presence_penalty` parameter with different range (-2.0 to 2.0)
)

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.
# For Anthropic and Gemini this parameter will be ignored
