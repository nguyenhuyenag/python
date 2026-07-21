from google import genai

client = genai.Client(api_key="AQ.Ab8RN6LFnemqJmP51Xo8p3BAZc5eoUiwEG82IoM4GF9fzMUHmA")

# for model in client.models.list():
#     print(model.name)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Expand of expression (a+b+c)^2"
)

print(response.text)