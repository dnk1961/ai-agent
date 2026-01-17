import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from system_prompt import system_prompt
from call_function import available_functions

def ask_gemini(client, messages):

    resp = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions]),

    )
    return resp

def main():
    #CLI Argument Parser
    parser = argparse.ArgumentParser(description="Gemini Chatbot")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    #Client Instance
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    #Message Arguement
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    #Send Query
    response = ask_gemini(client, messages)
    #Print Results
    if args.verbose:
        print(f"User prompt: {response.text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if not response.function_calls:
        print("Response:")
        print(response.text)
        return
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")

if __name__ == "__main__":
    main()
