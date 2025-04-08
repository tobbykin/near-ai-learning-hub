# ============================================================
# Carleton University Challenge: Implement the "quote" command.
#
# When a user sends a message containing "quote",
# your agent should fetch a motivational quote from an external API.
#
# Hints:
# 1. Use the 'requests' library for HTTP GET requests.
# 2. A suggested endpoint is:
#    https://api.quotable.io/random
# 3. Ensure the response is successful (status code 200).
# 4. Parse the JSON to extract the "content" (the quote) and "author".
#
# Useful resources:
# - Requests documentation: https://docs.python-requests.org/en/latest/
# - Quotable API: https://api.quotable.io/
# ============================================================

import requests
from nearai.agents.environment import Environment


def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif "quote" in message:
        try:
            response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")
            if response.status_code == 200:
                data = response.json()
                # The API returns an array of quotes, so we take the first one
                if data and isinstance(data, list) and len(data) > 0:
                    quote_data = data[0]
                    content = quote_data.get("quote")
                    author = quote_data.get("author")
                    if content and author:
                        return f"Breaking Bad Quote: \"{content}\" - {author}"
                    else:
                        return "Sorry, I couldn't fetch a quote properly."
                else:
                    return "Sorry, the quote API didn't return any quotes."
            else:
                return f"Sorry, failed to fetch a quote. Status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Sorry, an error occurred while fetching the quote: {e}"
    else:
        return "I'm sorry, I didn't understand your message."

def run(env: Environment):
    messages = env.list_messages()
    if not messages:
        # Handle the case where there are no messages, maybe prompt for input or send a welcome message
        env.add_reply("Hello! Send me a message.")
        env.request_user_input() # Request input if no message history
        return

    # Get the last message, assuming it's from the user
    last_message = messages[-1]
    if last_message.get("role") == "user":
        user_input = last_message.get("content", "")
        reply = handle_message(user_input)
        env.add_reply(reply)
    else:
        # Handle cases where the last message isn't from the user, or decide how to proceed
        # For now, let's just request input again if the last message wasn't from the user
        env.request_user_input()

# No explicit run(env) call here if this is meant to be imported or run differently by the platform
# If this script is run directly, you might need the environment setup.
# For the challenge context, assuming the run function is called by the platform.

run(env)