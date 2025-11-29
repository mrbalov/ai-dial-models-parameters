import os
from task.app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#  chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

N_MIN = 1
N_MAX = 3

deployment_name = os.getenv('DIAL_DEPLOYMENT_NAME', 'gpt-4o')
n = int(os.getenv('DIAL_N', '1'))

if n < N_MIN or n > N_MAX:
    raise ValueError("The 'n' parameter must be in the range from 1 to 3")

run(
    # TODO:
    #  1. Provide `deployment_name` with model from the list above👆
    #  2. Use `n` parameter with value in range from 1 to 5!
    n=n,
    deployment_name=deployment_name,
    print_request=False, # Switch to False if you do not want to see the request in console
    print_only_content=False, # Switch to True if you want to see only content from response
)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
