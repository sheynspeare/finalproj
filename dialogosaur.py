import google.generativeai as genai

genai.configure(
    api_key = API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "Respond as if you're explaining things to a ten-year-old kid"

while (True):
  question = input("You: ")

  if(question.strip() == ''):
    break

  response = chat.send_message(instruction + question)
  print(f"Dialogosaur: {response.text}")
  print('\n')
  instruction = ''