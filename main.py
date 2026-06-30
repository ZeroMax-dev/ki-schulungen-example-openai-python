from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client (reads the API key from the environment)
client = OpenAI(
    # base_url="http://127.0.0.1:1234/v1",  # uncomment to target a local model server
    api_key=os.getenv("OPENAI_API_KEY")
)

# We use the Responses API (client.responses.create), OpenAI's current
# recommended interface. Docs: https://developers.openai.com/api/docs/guides/text
response = client.responses.create(
    model="gpt-4o-mini",
    # `input` can be a plain string or a list of role-based messages
    input=[
        # system message first, it helps set the behavior of the assistant
        {"role": "system", "content": "You are a helpful assistant."},
        # I am the user, and this is my prompt
        {"role": "user", "content": "What's the best star wars movie?"},
        # we can also add the previous conversation
        # {"role": "assistant", "content": "Episode III."},
    ],
)
# let's see the reply (output_text joins all text output from the model)
print(response.output_text)
# e.g. "Many critics and fans consider 'The Empire Strikes Back' the best Star Wars movie."
