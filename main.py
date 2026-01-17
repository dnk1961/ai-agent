import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from system_prompt import system_prompt
from call_function import available_functions, ask_gemini, call_function

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
    for _ in range(20):
        #Send Query
        response = ask_gemini(client, messages)
        #Saving previous context
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate)
        results = []
        #Print Results
        verbose = False
        if args.verbose:
            verbose = True
            print(f"User prompt: {response.text}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
        if not response.function_calls:
            print("Final Response:")
            print(response.text)
            return
        
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose)
            if function_call_result.parts is None:
                raise Exception(f"Function call result PARTS is empty")
            if function_call_result.parts[0].function_response is None:
                raise Exception(f"Function call response part 2 is empty")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception(f"Response Part 3 is empty")
            if verbose is True:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            results.append(function_call_result.parts[0])
            messages.append(types.Content(role="user", parts=results))
    if response.function_calls:
        sys.exit(1)
    else:
        sys.exit(0)
if __name__ == "__main__":
    main()
