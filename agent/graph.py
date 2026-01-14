from langgraph.graph import StateGraph

from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture
from agent.llm import llm


def chatbot_node(state: AgentState):
    user_msg = state["messages"][-1]

    # 🔒 Lock intent once high-intent is detected
    if state.get("intent") != "high_intent":
        state["intent"] = detect_intent(user_msg)

    intent = state["intent"]

    if intent == "greeting":
        try:
            response = llm.invoke(
                "Greet the user briefly and ask what you can help with, such as pricing or plans."
            ).content
        except Exception:
            response = "Hi! How can I help you today? Would you like to know about our pricing or plans?"

    elif intent == "product_inquiry":
        response = retrieve_answer(user_msg)

    elif intent == "high_intent":
        if not state.get("name"):
            response = "Great! May I have your name?"
        elif not state.get("email"):
            response = "Thanks! Please share your email."
        elif not state.get("platform"):
            response = "Which creator platform do you use? (YouTube, Instagram, etc.)"
        else:
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )
            response = "You're all set! Our team will contact you shortly."

    else:
        try:
            response = llm.invoke(
                f"The user said: '{user_msg}'. Ask politely what help they need, such as pricing or plans."
            ).content
        except Exception:
            response = "I can help with pricing, plans, or getting you started. What would you like to know?"


    state["messages"].append(response)
    return state


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("chatbot", chatbot_node)
    graph.set_entry_point("chatbot")
    graph.set_finish_point("chatbot")
    return graph.compile()
