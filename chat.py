import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyArJ7hpndStqeiASr8V2QV7t8bdpXHsZdI")

generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="youre a donkey who was struck by lightning and can talk now. ur wierdly wise and cnstantly judge my life choices\n",
)

history = []
print("sir.donke: sup")

while True:

  user_input = input("you: ")

  chat_session = model.start_chat(
    history=history 
  )

  response = chat_session.send_message(user_input)

  model_response = response.text

  print(f"sir.donke: {model_response}")
  print()

  history.append({"role":"user", "parts": [user_input]})
  history.append({"role":"model", "parts": [model_response]})