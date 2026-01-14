def detect_intent(user_message: str) -> str:
    msg = user_message.lower()

    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in msg for word in ["pricing", "price", "plans", "cost", "features"]):
        return "product_inquiry"

    if any(word in msg for word in ["try", "sign up", "subscribe", "use pro"]):
        return "high_intent"

    return "unknown"

