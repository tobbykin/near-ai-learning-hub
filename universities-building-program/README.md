# Near AI Agent Building Program: Customize Your NEAR AI Agen

After deploying your first NEAR AI Agent using the [Getting Started with NEAR AI](https://github.com/TheBAFNetwork7/near-ai-learning-hub/blob/main/tutorials/getting-started-with-near-ai.md) tutorial, your next challenge is to extend your agent’s functionality. For this workshop, each participating university will work on a specific Python file provided in our repository. These files have been prepared with an incomplete implementation that you must complete to add a new command:

- **Emory University:** Complete the `"joke"` command – the agent should fetch a random joke from an external API.
- **Carleton University:** Complete the `"quote"` command – the agent should fetch a motivational quote from an external API.
- **Columbia University:** Complete the `"weather"` command – the agent should fetch live weather data (temperature and conditions) for a given city.

After you complete your task, test your updated agent locally and submit a pull request. Only those who submit a pull request will be considered for a bounty prize!

## Overview

### 1. Initial Setup:

You’ve already deployed your first NEAR AI Agent locally by following the [Getting Started with NEAR AI](https://github.com/TheBAFNetwork7/near-ai-learning-hub/blob/main/tutorials/getting-started-with-near-ai.md) tutorial.
    
### 2. Repository Cloning:

To participate, you must clone the entire repository. This is essential since only a cloned repository allows you to push changes and submit a pull request.
    
### 3. University-Specific Customization:
    
In the cloned repository, navigate to the `universities-building-program` folder and find the file corresponding to your university:
    
- **Emory University:** `emory.py`
- **Carleton University:** `carleton.py`
- **Columbia University:** `columbia.py`
  
### 4. Implementation:
    
Each file contains a partially implemented `handle_message` function with clear TODO comments. Your task is to complete the missing functionality (without copying full solutions from online sources) following the provided hints.
    
### 5. Testing and Submission:
    
Replace your local agent’s code with the updated file, test it interactively, and then submit a pull request to the main repository. Only participants who submit a pull request will be entered into the bounty drawing.
    

## Detailed Steps

### Step 1: Verify Your Initial Deployment

Before you start, make sure your first NEAR AI Agent is running locally. Open your terminal and run:

```bash
nearai agent interactive ~/.nearai/registry/your_wallet.near/my_first_agent/0.0.1 --local
```

Confirm that you can interact with your agent.

---

### Step 2: Clone the Repository

It is crucial to clone the repository so that you can later push your modifications.

1. **Clone the Repository:**
    
    ```bash
    git clone https://github.com/TheBAFNetwork7/near-ai-learning-hub.git
    ```
    
2. **Navigate to the University Folder:**
    
    ```bash
    cd near-ai-learning-hub/universities-building-program
    ```
    
3. **Copy Your University File to Your Agent Directory:**
    
    For example, if you are representing Emory, run:
    
    ```bash
    cp emory.py ~/my_near_agent/agent.py
    ```
    
    (Make sure you adjust the file path according to your local environment.)
    
---

### Step 3: Customize Your Agent

1. **Open the File in an Editor:**
    
    Open the copied file (e.g., `agent.py`) in your preferred text editor.
    
2. **Examine the Incomplete Code:**
    
    You will see a function similar to this:
    
    ```python
    def handle_message(message: str) -> str:
        message = message.lower()
        if "hello" in message:
            return "Hello, welcome to NEAR AI!"
        elif "joke" in message:
            # TODO: Implement the joke command.
            # Hints: Use Python’s requests library to call a public joke API.
            pass
        else:
            return "I'm sorry, I didn't understand your message."
    ```
    
    The file you work on depends on your university. For Carleton and Columbia, the file will prompt you to implement the `"quote"` or `"weather"` command, respectively.
    
3. **Implement the Missing Functionality:**
    
    Use the hints provided in the file. For instance, for the `"joke"` command, figure out how to send an HTTP GET request to an appropriate public joke API and parse the JSON response. The goal is to encourage independent problem solving without giving away a full solution.
    
4. **Save Your Changes:**
    
    Once you’ve implemented your command(s), save the file.

---

### Step 4: Test Your Customized Agent Locally

1. **Deploy Your Updated Agent:**
    
    Replace your current agent file with your customized file.
    
2. **Run the NEAR AI Interactive Command:**
    
    ```bash
    nearai agent interactive ~/.nearai/registry/your_wallet.near/my_first_agent/0.0.1 --local
    ```
    
3. **Interact with Your Agent:**
    
    Test your implementation by typing:
    
    - `"joke"` if you’re at Emory.
    - `"quote"` if you’re at Carleton.
    - `"weather London"` (or another city) if you’re at Columbia.
    
    Ensure that the agent responds as expected.

---

### Step 5: Submit Your Changes

1. **Commit Your Modifications:**
    
    ```bash
    git add .
    git commit -m "University Challenge: Customized agent for [Your University] with [joke/quote/weather] command"
    ```
    
2. **Push Your Changes:**
    
    ```bash
    git push origin main
    ```
    
3. **Submit a Pull Request:**
    
    Navigate to the GitHub page for the near-ai-learning-hub repository and submit a pull request with your modifications. Only those who submit a pull request will be considered for the bounty prize.
    

## Additional Resources

- **NEAR AI Documentation:**
    - [NEAR AI Agents Documentation](https://docs.near.ai/agents/)
    - [NEAR AI Agents Registry Documentation](https://docs.near.ai/agents/registry/#uploading-an-agent)
    - [NEAR AI Inference and Environment Docs](https://docs.near.ai/agents/env/inference/)
- **GitHub Guides:**
    - [Forking a Repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
    - [Creating Pull Requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)

## Wrap-Up

At the conclusion of the workshop, we will review the process together:

- Discuss each enhancement and the challenges you faced.
- Share experiences and creative approaches.
- Remember, only those who submit a pull request will be entered into the bounty drawing for a special prize.

Enjoy the challenge, learn from it, and happy coding! 🛠️
