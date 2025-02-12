from openai import OpenAI
import os
from google.cloud import secretmanager
import argparse


def get_secret(secret_name):
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    client = secretmanager.SecretManagerServiceClient()
    secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(request={"name": secret_path})
    return response.payload.data.decode("UTF-8")

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
MAX_INPUT_LENGTH = 12
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input" , "-i", type = str, required=True)
    args = parser.parse_args()
    user_input = args.input
    if validate_length(user_input):
        print(f"User input : {user_input}")
        generate_response(user_input)
    else:
        raise ValueError("Input must be under 12 tokens !")

def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH

def generate_response(prompt : str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful IT assistant."},
            {
                "role": "user",
                "content": f"Generate a concise explanation of {prompt} in under 50 tokens"
            }
        ],
        max_tokens=50
    )
    response = completion.choices[0].message.content
    print(response)
    return response

if __name__ == "__main__" :
    main()