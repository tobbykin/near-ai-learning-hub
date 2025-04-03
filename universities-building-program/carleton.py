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

def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif "quote" in message:
        # TODO: Implement the quote command.
        # Steps:
        #   1. Use requests.get() to call the quote API.
        #   2. Check if the response is OK (status code 200).
        #   3. Parse the JSON response to retrieve the "content" and "author".
        #   4. Return a formatted string with the quote and its author.
        pass
    else:
        return "I'm sorry, I didn't understand your message."

# Optional testing block:
# if __name__ == "__main__":
#    user_input = input("Enter a message for the agent: ")
#    print(handle_message(user_input))
