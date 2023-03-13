import openai
openai.api_key = "ADD_KEY_HERE"
# Choose a model
MODEL_ENGINE = "text-davinci-003"

def get_response(prompt):
    """Returns the response for the given prompt using the OpenAI API."""
    completions = openai.Completion.create(
             engine = MODEL_ENGINE,
             prompt = prompt,
         max_tokens = 1024,
        temperature = 0.7,
    )
    print ("get_response")
    return completions.choices[0].text

def handle_input(
               input_str : str,
    conversation_history : str,
                USERNAME : str,
                 AI_NAME : str,
                 ):
    print ("handle_input")
    """Updates the conversation history and generates a response using GPT-3."""
    # Update the conversation history
    conversation_history += f"{USERNAME}: {input_str}\n"
   
    # Generate a response using GPT-3
    message = get_response(conversation_history)

    # Update the conversation history
    conversation_history += f"{AI_NAME}: {message}\n"

    # Print the response
    print(f'{AI_NAME}: {message}')
    
    return conversation_history

# Set the initial prompt to include a personality and habits
INITIAL_PROMPT = ('''
    I am a friendly artificial intelligence.
''')
conversation_history = INITIAL_PROMPT + "\n"

USERNAME = "USER"
AI_NAME = "AI"

while True:
    # Get the user's input
    user_input = input(f"{USERNAME}: ")

    # Handle the input
    handle_input(user_input, conversation_history, USERNAME, AI_NAME)