from os import getenv
from random import uniform
from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

FP_MIN = -2.0
FP_MAX = 2.0

deployment_name = getenv('DIAL_DEPLOYMENT_NAME', 'gpt-4o')
frequency_penalty = float(getenv('DIAL_FREQUENCY_PENALTY', uniform(FP_MIN, FP_MAX)))

run(
    deployment_name=deployment_name,
    print_only_content=True,
    frequency_penalty=frequency_penalty,
    # TODO:
    #  Use `frequency_penalty` parameter with different range (-2.0 to 2.0).
)

# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored
