import json

def load_knowledge():
    with open("data/knowledge_base.json") as f:
        return json.load(f)

def retrieve_answer(query: str):
    q = query.lower()

    if any(word in q for word in ["price", "pricing", "plan", "plans", "cost"]):
        return (
            "Here are our AutoStream plans:\n\n"
            "🔹 Basic Plan – $29/month\n"
            "- 10 videos/month\n"
            "- 720p resolution\n\n"
            "🔹 Pro Plan – $79/month\n"
            "- Unlimited videos\n"
            "- 4K resolution\n"
            "- AI captions\n"
            "- 24/7 Pro support"
        )

    if "refund" in q:
        return "We offer no refunds after 7 days."

    if "support" in q:
        return "24/7 support is available only on the Pro plan."

    return "I can help with pricing, plans, and policies."
