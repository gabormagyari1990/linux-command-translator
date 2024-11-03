# Linux Command Translator

A simple terminal application that translates natural language instructions into Linux commands using OpenAI's GPT-4.

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```
   cp .env.example .env
   ```
4. Edit `.env` and replace `your-api-key-here` with your actual OpenAI API key

## Usage

1. Run the translator:
   ```
   python translate.py
   ```
2. Enter your instruction in natural language (e.g., "show me all running processes")
3. Review the translated command
4. Confirm whether you want to execute it

Type 'exit' to quit the application.

## Features

- Translates natural language to Linux commands using GPT-4
- Shows the translated command before execution
- Asks for confirmation before running any command
- Displays command output and any errors
- Simple and safe to use
