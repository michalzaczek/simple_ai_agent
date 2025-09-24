import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    sys_args = sys.argv
    model = "gemini-2.0-flash-001"

    if len(sys_args) < 2:
        print("Error: no prompt provided!")
        sys.exit(1)

    user_prompt = sys_args[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(model=model, contents=messages)
    usage_metadata = response.usage_metadata
    prompt_tokens = usage_metadata.prompt_token_count
    response_tokens = usage_metadata.candidates_token_count

    print(response.text)

    if len(sys_args) > 2 and sys_args[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
