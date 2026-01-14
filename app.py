from dotenv import load_dotenv
load_dotenv()

from agent.graph import build_graph

graph = build_graph()

state = {
    "messages": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

print("AutoStream Agent Started (type 'exit' to stop)\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    state["messages"].append(user_input)

    # ✅ Capture lead info ONLY after high-intent
    if state["intent"] == "high_intent":
        if not state["name"]:
            state["name"] = user_input
        elif not state["email"]:
            state["email"] = user_input
        elif not state["platform"]:
            state["platform"] = user_input

    state = graph.invoke(state)
    print("Agent:", state["messages"][-1])
