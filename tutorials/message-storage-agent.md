# Designing a Secure AI Agent for Decentralized Systems: Verified Messaging and Persistent Storage

In decentralized systems such as NEAR, AI agents exchange data using a structured messaging model. In this guide, we explain how to build a simple Python-based AI agent that creates, verifies, and persistently stores messages. This process is essential for ensuring data integrity, secure inter-agent communication, and maintaining historical context for advanced processing.

## What Is NEAR’s Messaging Model?

NEAR’s messaging model uses **message files** composed of three main components:

- **Header:**
Contains metadata such as the sender, recipient, timestamp, and a unique message ID. This metadata makes every message traceable and unique.
    
- **Payload:**
This is the content of the message. It carries commands or data that the agent must process. For example, a command to store specific data.
    
- **Signature:**
A cryptographic hash (using SHA256 in our example) computed over the header and payload. The signature guarantees that if any part of the message is altered, the signature will not match, thereby alerting the system to potential tampering.

By following this structure, agents can be confident that their communications are authentic and have not been modified in transit.

## Why Is This Important?

Consider a system where multiple agents interact:

- Every message is signed, so recipients know the data has not been changed.
- Persistently storing messages (simulated here with a JSON file) allows an agent to “remember” past interactions. This historical data can later be used to enhance advanced processing, such as providing context for language model inference.
- Understanding this model is crucial for developing robust, decentralized AI systems on NEAR.

## Let's Build the Agent 😼🛠️

Our Python-based AI agent will perform the following tasks:

1. Construct a message with a header, payload, and signature.
2. Verify that the message has not been altered.
3. Store the message persistently (simulating on-chain storage).
4. Retrieve stored messages to provide historical context.

### Step 1: Environment Setup

1. **Create a Project Directory:**
    
    ```
    mkdir near-ai-agent-storage
    cd near-ai-agent-storage
    ```
    
2. **(Optional) Create and Activate a Virtual Environment:**
    
    ```
    python3 -m venv env
    source env/bin/activate
    ```
    
3. This guide uses standard Python libraries (`json`, `time`, `hashlib`, and `os`), so no additional installations are required.

### Step 2: Building the Agent

Create a file named `agent.py` with the following code. The code is extensively commented to explain each step clearly.

```python
import json
import time
import hashlib
import os

# File to simulate persistent storage (analogous to on-chain storage)
STORAGE_FILE = 'message_storage.json'

class NearAgent:
    def __init__(self, agent_id):
        # Initialize the agent with its unique identifier.
        self.agent_id = agent_id

    def create_message(self, recipient, command, data, message_id):
        """
        Create a message using NEAR's messaging model.

        Structure:
        - Header: Contains sender, recipient, timestamp, and message ID.
          * Ensures traceability and uniqueness.
        - Payload: Contains the command and data.
          * Represents the actionable part of the message.
        - Signature: A SHA256 hash over the header and payload.
          * Guarantees message integrity.

        Returns:
            A dictionary representing the complete message.
        """
        header = {
            "sender": self.agent_id,         # ID of the sending agent
            "recipient": recipient,          # Target agent
            "timestamp": int(time.time()),   # Creation time (epoch timestamp)
            "message_id": message_id         # Unique message identifier
        }
        payload = {
            "command": command,              # Action to perform (e.g., "store_data")
            "data": data                     # Associated data (e.g., {"info": "sample data"})
        }
        message = {"header": header, "payload": payload}
        # Serialize message with sorted keys for consistency
        message_str = json.dumps(message, sort_keys=True).encode()
        # Create a cryptographic signature using SHA256
        signature = hashlib.sha256(message_str).hexdigest()
        message["signature"] = signature
        return message

    def verify_message(self, message):
        """
        Verify the integrity of a message by re-calculating its signature.

        Process:
        1. Extract the signature from the message.
        2. Remove the signature field.
        3. Serialize the remaining content.
        4. Compute the SHA256 hash.
        5. Compare the computed hash with the extracted signature.

        Returns:
            True if the signature matches; False otherwise.
        """
        provided_signature = message.get("signature")
        message_copy = message.copy()
        message_copy.pop("signature", None)  # Exclude signature for recalculation
        message_str = json.dumps(message_copy, sort_keys=True).encode()
        calculated_signature = hashlib.sha256(message_str).hexdigest()
        return provided_signature == calculated_signature

    def store_message(self, message):
        """
        Store the message persistently by appending it to a JSON file.
        This simulates on-chain storage, maintaining a historical record.
        """
        if os.path.exists(STORAGE_FILE):
            with open(STORAGE_FILE, 'r') as f:
                messages = json.load(f)
        else:
            messages = []
        messages.append(message)
        with open(STORAGE_FILE, 'w') as f:
            json.dump(messages, f, indent=2)
        print("Message stored successfully.")

    def load_messages(self):
        """
        Retrieve all stored messages.

        Returns:
            A list of messages; an empty list if none exist.
        """
        if os.path.exists(STORAGE_FILE):
            with open(STORAGE_FILE, 'r') as f:
                return json.load(f)
        return []

    def process_message(self, message):
        """
        Process an incoming message by:
        1. Verifying its integrity.
        2. Storing it persistently.
        3. If the command is "store_data", generating an acknowledgment.

        Returns:
            The response message if applicable; otherwise, None.
        """
        if not self.verify_message(message):
            print("Invalid message signature!")
            return None

        sender = message["header"]["sender"]
        print(f"Processing message from {sender}")
        self.store_message(message)

        if message["payload"]["command"] == "store_data":
            response_data = {"status": "data stored", "timestamp": int(time.time())}
            response = self.create_message(
                recipient=sender,
                command="acknowledge",
                data=response_data,
                message_id=f"resp_{message['header']['message_id']}"
            )
            self.store_message(response)
            return response
        else:
            print("Unknown command.")
            return None

    def simulate(self):
        """
        Simulate the full messaging cycle:
        - Create an incoming message from an external agent ("agent2").
        - Process the message (verification, storage, response).
        - Print the incoming message, response, and all stored messages.
        """
        # Create a message intended for this agent with the command "store_data"
        incoming_message = self.create_message(
            recipient=self.agent_id,
            command="store_data",
            data={"info": "sample persistent data"},
            message_id="msg_001"
        )
        # Modify the sender to simulate that the message comes from "agent2"
        incoming_message["header"]["sender"] = "agent2"
        # Recalculate the signature due to the change in the header
        message_str = json.dumps({
            "header": incoming_message["header"],
            "payload": incoming_message["payload"]
        }, sort_keys=True).encode()
        incoming_message["signature"] = hashlib.sha256(message_str).hexdigest()

        print("Incoming Message:")
        print(json.dumps(incoming_message, indent=2))
        response = self.process_message(incoming_message)
        if response:
            print("Response Message:")
            print(json.dumps(response, indent=2))

        print("\nAll Stored Messages:")
        stored_messages = self.load_messages()
        print(json.dumps(stored_messages, indent=2))

if __name__ == "__main__":
    # Initialize the agent with the ID "agent1" and run the simulation
    agent = NearAgent("agent1")
    agent.simulate()

```

## What’s Happening Under the Hood?

1. The `create_message` method builds a message with a header, payload, and a signature calculated using SHA256. This signature ensures that any changes to the message can be detected.
    
2. The `verify_message` method recalculates the signature after stripping the original signature. If they match, the message is confirmed as unaltered.
    
3. Messages are stored in a JSON file via the `store_message` method. This simulates a persistent storage solution, allowing your agent to retain historical data.
    
4. When processing an incoming message, the agent verifies its integrity, stores it, and if the command is `"store_data"`, generates an acknowledgment response. The `simulate` function demonstrates this full cycle by printing the incoming message, the response, and all stored messages.

## Running the Exercise

1. **Run the Agent:**
    
    Open a terminal in your project directory and run:
    
    ```bash
    python agent.py
    ```
    
2. **Expected Output:**
    - The "Incoming Message" will display the message details (header, payload, and signature).
    - The agent will print a processing log, indicating successful verification.
    - If the command is `"store_data"`, an acknowledgment response will be generated and stored.
    - Finally, the agent prints all stored messages, showing the full history.


## Wrapping Up

By completing this exercise, you now understand:

- How NEAR's messaging model uses a header, payload, and signature to ensure secure communication.
- The importance of persistent storage for maintaining context in decentralized systems.
- How a practical implementation of these concepts can form the basis for more advanced features like context-aware LLM inference.
