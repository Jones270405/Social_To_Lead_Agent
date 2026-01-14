# Conversational AI Agent

## 1. How to Run the Project Locally

1. *Clone the repository:*
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>

3. *Create a virtual environment:*
   
    python -m venv venv
   
    source venv/bin/activate  # For Linux/Mac
   
    venv\Scripts\activate     # For Windows

5. *Install dependencies:*
   
    pip install -r requirements.txt

7. *Run the application:*
   
    python app.py

9. Open your terminal or preferred interface and interact with the agent.

2. **Architecture Explanation**
This project leverages LangGraph and AutoGen to build a conversational AI agent capable of knowledge retrieval, intent detection, and tool execution.

*Why LangGraph / AutoGen:*
LangGraph enables modular design of agent workflows through nodes and edges, allowing us to define conversation flows, knowledge retrieval, and tool execution in a structured manner. AutoGen simplifies multi-step interactions by automating prompt management and chaining tasks while maintaining context.

*State Management:*
State is managed using an internal memory object that tracks user inputs, conversation history, and extracted entities. For example, when the user provides their name and email, the agent stores these details in memory. This allows the agent to persist information across multiple turns, dynamically adjust its responses, and trigger actions like mock_lead_capture() when the lead is qualified.

This architecture ensures modularity, scalability, and easy debugging, making it simple to extend the agent with additional intents, tools, or knowledge sources.

3. **WhatsApp Deployment**
To integrate this agent with WhatsApp, you can use the WhatsApp Business API or Twilio WhatsApp with webhooks:

Set up a webhook URL in your server that listens for incoming WhatsApp messages.

When a user sends a message, WhatsApp forwards it to your webhook.

The webhook handler passes the message to your agent, which processes it (RAG, intent detection, lead capture, etc.).

The agent generates a response and sends it back to the user via the WhatsApp API.

This setup allows the conversational agent to function seamlessly on WhatsApp, handling messages, retrieving knowledge, qualifying leads, and executing tools in real-time.
