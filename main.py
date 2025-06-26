import os
import argparse
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
parser = argparse.ArgumentParser()
parser.add_argument("prompt")
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()

if not args.prompt:
  raise Exception("no prompt given")
prompt = args.prompt
if args.verbose:
  print(f"User prompt: {prompt}")

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
  ]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
print(response.text)
if args.verbose:
  print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
  print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

