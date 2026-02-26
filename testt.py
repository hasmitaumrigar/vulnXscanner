import os
from google import genai
# Create client with API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Send request to Gemini 2.5 Flash
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain SQL Injection in simple cybersecurity terms."
)

print("\n=== Gemini Response ===\n")
print(response.text)