import os
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError(
        "Gemini API key not found. Set GOOGLE_API_KEY as an environment variable."
    )

llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro",   # ✅ STABLE FREE MODEL
    temperature=0.3,
    google_api_key=api_key
)
