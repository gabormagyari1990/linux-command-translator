#!/usr/bin/env python3
import os
import openai
from dotenv import load_dotenv
import subprocess

def setup():
    """Load environment variables and configure OpenAI client."""
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key like this:")
        print("OPENAI_API_KEY=your-api-key-here")
        exit(1)
    return openai.OpenAI(api_key=api_key)

def get_command_translation(client, instruction):
    """Translate natural language to Linux command using OpenAI API."""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Linux command translator. Convert natural language instructions to appropriate Linux shell commands. Provide ONLY the command, no explanations."},
                {"role": "user", "content": instruction}
            ],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error while translating: {str(e)}")
        return None

def main():
    """Main function to run the translator."""
    client = setup()
    
    print("\n=== Linux Command Translator ===")
    print("Type 'exit' to quit\n")
    
    while True:
        # Get user instruction
        instruction = input("\nEnter your instruction: ")
        
        if instruction.lower() == 'exit':
            break
            
        if not instruction.strip():
            continue
            
        # Get command translation
        command = get_command_translation(client, instruction)
        
        if not command:
            continue
            
        # Show the translated command and ask for confirmation
        print(f"\nTranslated command: {command}")
        confirm = input("\nDo you want to execute this command? (y/N): ")
        
        if confirm.lower() == 'y':
            try:
                # Execute the command
                result = subprocess.run(command, shell=True, text=True, capture_output=True)
                print("\nOutput:")
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print("Errors:", result.stderr)
            except Exception as e:
                print(f"Error executing command: {str(e)}")
        else:
            print("Command execution cancelled.")

if __name__ == "__main__":
    main()
